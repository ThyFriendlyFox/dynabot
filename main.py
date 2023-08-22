import os
import openai
from dotenv import load_dotenv
from spinner import Spinner

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key from .env or set it directly
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get the engine from the .env file
ENGINE = os.getenv('ENGINE', 'gpt-3.5-turbo')

# Path to the Library Functions directory
LIBRARY_PATH = "Library Functions"

# Load function descriptions
with open(os.path.join(LIBRARY_PATH, "description.txt"), "r") as f:
    descriptions = f.readlines()

# Dictionary to store function details
function_details = {}
for line in descriptions:
    parts = line.strip().split(":")
    function_details[parts[0].strip()] = parts[1].strip()

def invoke_function(function_name):
    # Dynamically import the function module
    module = __import__(f"Library_Functions.{function_name}", fromlist=[function_name])
    # Get the function from the module
    function = getattr(module, function_name)
    # Invoke the function
    return function()

def interact_with_llm():
    print("Welcome to the LLM CLI! Type 'exit' to quit.")
    
    # Initialize chat sequence with a system message
    chat_sequence = [{"role": "system", "content": f"You are a helpful assistant that can invoke functions from the Library Functions folder. The available functions are: {', '.join(function_details.keys())}."}]
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for exit command
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Add user message to chat sequence
        chat_sequence.append({"role": "user", "content": user_input})
        
        # Get response using ChatCompletion API
        response = openai.ChatCompletion.create(model=ENGINE, messages=chat_sequence)
        
        # Extract assistant's message
        assistant_message = response['choices'][0]['message']['content']
        
        # Check if the user asks about available functions
        if "functions" in user_input and "library" in user_input:
            print(f"LLM: The available functions in the Library Functions folder are: {', '.join(function_details.keys())}.")
            continue
        
        # Check if the assistant suggests invoking a function
        if "invoke" in assistant_message:
            function_name = assistant_message.split(" ")[-1]  # Extract the function name from the assistant's message
            if function_name in function_details:
                result = invoke_function(function_name)
                print(f"LLM: {result}")
                continue
            else:
                print(f"LLM: I'm sorry, I couldn't find a function named {function_name} in the Library Functions folder.")
                continue
        
        # If no function invocation is suggested, print the assistant's response
        print(f"LLM: {assistant_message}")

if __name__ == "__main__":
    interact_with_llm()
