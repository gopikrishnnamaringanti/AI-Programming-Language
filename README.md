# MyOPL – AI-Assisted Pseudo Code Programming Language

## About

**MyOPL** (My Own Pseudo Language) is a **custom programming language** designed with AI-powered assistance. It combines traditional programming constructs with **pseudo-code-like structures**, allowing both beginners and advanced users to write, edit, and execute code seamlessly.  

The language includes:

- **Lexer, parser, compiler, and interpreter** (implemented in `basic.py`)  
- **Tokens and grammar definitions** for structured pseudo-code execution  
- **AI-powered code completion and suggestions** using Google Gemini LLM  
- **Interactive shell** with multi-line editing, save/load functionality, and timing for execution  

MyOPL is ideal for **learning programming concepts**, **rapid prototyping**, and exploring **AI-assisted programming workflows**.

---

## Features

- **Write Code:** Create new `.myopl` files with pseudo-code.  
- **Edit Code:** Interactive editing with `prompt_toolkit` (`Ctrl-S` to save, `Ctrl-C / Ctrl-Q` to exit).  
- **AI Code Completion:** Ask the AI to complete, suggest, or optimize code.  
- **Run Code:** Execute pseudo-code using `basic.py` interpreter.  
- **Lexer & Parser:** Full lexical analysis and parsing for custom pseudo-code grammar.  
- **Compiler:** Converts pseudo-code into executable instructions in the interpreter.  
- **Token Management:** Define, identify, and validate tokens for structured programming.  
- **Call API from File:** Send `.myopl` file content to AI for suggestions or explanations.  
- **Execution Timing:** Automatic measurement of function and command execution times.  
- **Pseudo-Code Language Syntax:** Flexible and human-readable syntax for learning and AI-assisted coding.  

---

## Tech Stack

- **Language:** Python 3.11+  
- **AI Integration:** Google Gemini LLM (`google.generativeai`)  
- **Interactive Shell:** `prompt_toolkit`  
- **Interpreter/Compiler:** `basic.py` implements lexers, parsers, tokens, grammar, and execution engine  
- **Time Tracking:** Python `time` module  
- **Shell Execution:** Python `subprocess`  

---

## Installation

### Clone the repository

```bash
git clone <your-repo-url>
cd MyOPL

basic > writecode
Enter the filename (without extension): example
Enter your code below. Type 'SAVE' on a new line to finish.
PRINT "Hello, World!"
SAVE
Code saved to example.myopl

basic > editcode
Editing (Ctrl-S to save, Ctrl-C to exit):
# Modify code interactively

basic > callai
Enter prompt for AI: Add input handling and print square of input
# AI generates code step-by-step

basic > apifromfile example
Enter additional prompt: Optimize this code
# AI suggests improvements
