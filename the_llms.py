"""The fundamental component of LangChain involves invoking an LLM with a specific input. To illustrate this, we'll explore a simple example. Let's imagine we are building a service that suggests personalized workout routines based on an individual's fitness goals and preferences.

To accomplish this, we will first need to import the LLM wrapper.
"""

# Import necessary libraries
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

# Load the OpenAI API key from the .env file
# This will read the .env file in the current directory
load_dotenv()  
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI LLM with specific settings
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

# Define the input text
text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."

# Call the LLM and print the output
output = llm(text)
print(output)
