# DynaBot

DynaBot, A Modular, Simple Autonomous Agent Framework Utilizing Localized Function Calling, is an interactive command-line interface (CLI) tool powered by OpenAI's GPT-3.5-turbo engine. It's designed to assist users by invoking specific functions from a predefined library based on user input.

## Features

- **Interactive CLI**: Engage in a conversational manner with the bot.
- **Function Invocation**: Dynamically call functions from the "Library Functions" folder based on user intent.
- **OpenAI Integration**: Utilizes OpenAI's GPT-3.5-turbo engine for understanding and generating responses.

## Setup

1. **Environment Setup**:
   - Clone the repository with `git clone https://github.com/ThyFriendlyFox/dynabot.git`
   - Install the required packages using `pip install -r requirements.txt`.
   - Set up a `.env` file in the root directory with your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

2. **Running DynaBot**:
   - Navigate to the project directory in the terminal.
   - Run `python main.py` to start the interactive CLI.

## Function Library

DynaBot can invoke functions from the "Library Functions" folder. The descriptions and details of these functions are stored in `descriptions.txt`.

## Usage

After starting DynaBot, you can interact with it using natural language. For example:
`
You: Hello! What functions are available in your function library?
LLM: The available functions in the Library Functions folder are: web_scraper.py, api_parser.py, openai_interaction.py, loop_detection.py.
You: Can you search the web for Wikipedia Articles about Steel?    
LLM: Sure! Let me fetch that information for you using the `web_scraper.py` function.
`
Please note, it may take a little while to run the functions. Please send feedback through the issues tab, and I will try to get to them as soon as possible.
