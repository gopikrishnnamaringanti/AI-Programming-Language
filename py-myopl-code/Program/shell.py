import os
import subprocess
import time
import google.generativeai as genai
from prompt_toolkit import PromptSession
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
genai.configure(api_key="")

def execute_write_code():
    filename = input("Enter the filename (without extension): ")
    if not filename.endswith('.myopl'):
        filename += '.myopl'

    print("Enter your code below. Press Enter to start a new line. Type 'SAVE' on a new line to finish.")
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    
    code = "\n".join(lines)
    
    with open(filename, 'w') as file:
        file.write(code)
    
    print(f"Code saved to {filename}")

def edit_code():
    filename = input("Enter the filename to edit (without extension): ")
    if not filename.endswith('.myopl'):
        filename += '.myopl'
    
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist.")
        return
    
    with open(filename, 'r') as file:
        content = file.read()
    
    session = PromptSession()
    bindings = KeyBindings()

    @bindings.add('c-c')
    @bindings.add('c-q')
    def exit_editor(event):
        """ Pressing Ctrl-C or Ctrl-Q will exit the editor. """
        event.app.exit()

    @bindings.add('c-s')
    def save_file(event):
        """ Pressing Ctrl-S will save the file. """
        buffer = event.app.current_buffer
        with open(filename, 'w') as file:
            file.write(buffer.text)
        print(f"\nCode saved to {filename}")
    
    document = Document(content)
    text = session.prompt('Editing (Ctrl-S to save, Ctrl-C to exit):\n', default=document.text, key_bindings=bindings, multiline=True)

    if text is not None:
        with open(filename, 'w') as file:
            file.write(text)

def create_model():
    """Creates and configures the generative model."""
    generation_config = {
        "temperature": 1.0,  # Adjust as needed
        "top_p": 1.0,  # Adjust as needed
        "top_k": 0,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }
    return genai.GenerativeModel(
        model_name="gemini-1.0-pro", generation_config=generation_config
    )

def call_api(prompt, model=None):
    """Sends a prompt to the generative model and prints response character by character."""
    if not model:
        model = create_model()
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    for char in response.text:
        print(char, end='')  # Print without newline
    print()  # Print newline after all characters
    return response.text

def call_api_from_file(filename, additional_prompt="", model=None):
    """Sends the content of a .myopl file as the prompt to the generative model."""
    file_path = None
    for file in os.listdir('.'):
        if file.startswith(filename) and file.endswith('.myopl'):
            file_path = file
            break
    
    if not file_path:
        print(f"File {filename}.myopl not found.")
        return
    
    with open(file_path, 'r') as file:
        prompt = file.read()

    prompt += additional_prompt

    return call_api(prompt, model)

def run_basic_shell():
    """Main loop for the basic shell."""
    import basic
    api_mode = False

    while True:
        if not api_mode:
            text = input('basic > ')
            if text.strip() == "":
                continue
            if text.lower() == "stop":
                break

            if text.lower()=="color":
                os.system('color f0')
            
            elif text.lower().startswith("writecode"):
                start_time_function = time.time()  # Start time of function execution
                execute_write_code()
                end_time_function = time.time()  # End time of function execution
                print(f"Function execution time: {end_time_function - start_time_function} seconds")
            elif text.lower().startswith("editcode"):
                start_time_function = time.time()  # Start time of function execution
                edit_code()
                end_time_function = time.time()  # End time of function execution
                print(f"Function execution time: {end_time_function - start_time_function} seconds")
            elif text.lower().startswith("apifromfile"):
                parts = text.strip().split(maxsplit=1)
                if len(parts) < 2:
                    print("Filename not provided.")
                    continue
                filename = parts[1]
                additional_prompt = input("Enter additional prompt: ")
                start_time_function = time.time()  # Start time of function execution
                call_api_from_file(filename, additional_prompt)
                end_time_function = time.time()  # End time of function execution
                print(f"Function execution time: {end_time_function - start_time_function} seconds")
            elif text.lower().startswith("callai"):
                api_prompt = input("Enter prompt for AI: ")
                start_time_function = time.time()  # Start time of function execution
                response = call_api(api_prompt)
                end_time_function = time.time()  # End time of function execution
                print(f"Function execution time: {end_time_function - start_time_function} seconds")
            else:
                result, error = basic.run('<stdin>', text)
                if error:
                    print(error.as_string())
                elif result:
                    if len(result.elements) == 1:
                        print(repr(result.elements[0]))
                    else:
                        print(repr(result))

            end_time_command = time.time()  # End time of command execution
        else:
            api_prompt = input("Enter prompt for AI: ")
            if api_prompt.lower() == "stop":
                api_mode = False
                continue
            response = call_api(api_prompt)
            print("Thinking... (Calling API)",end="\n")
            print(response)

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    subprocess.run(["start", "cmd", "/k", "run_basic.bat"], shell=True)
    
