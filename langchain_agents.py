"""
Agents in LangChain  

In LangChain, agents are high-level components that use language models (LLMs) to determine which actions to take and in what order. An action can either be using a tool and observing its output or returning it to the user. Tools are functions that perform specific duties, such as Google Search, database lookups, or Python REPL.  

Agents involve an LLM making decisions about which actions to take, taking that action, observing the result, and repeating the process until the task is completed.  

---

Types of Agents in LangChain  

1. Zero-Shot-React-Description Agent  
   - This agent uses the ReAct framework to decide which tool to employ based purely on the tool's description.  
   - It requires a description of each tool to function effectively.  

2. React-Docstore Agent  
   - This agent interacts with a document store (docstore) using the ReAct framework.  
   - It requires two tools:  
     - Search Tool: Finds a document.  
     - Lookup Tool: Searches for a term within the most recently found document.  

3. Self-Ask-With-Search Agent  
   - This agent employs a single tool named Intermediate Answer, which is capable of looking up factual responses to queries.  
   - It is identical to the original self-ask-with-search paper, where a Google Search API is provided as the tool.  

4. Conversational-React-Description Agent  
   - This agent is designed for conversational scenarios.  
   - It uses the ReAct framework to select a tool and incorporates memory to remember previous interactions in the conversation.  

---

Example Use Case  

In the following example, the agent will use the Google Search Tool to look up recent information about the Mars rover and generate a response based on this information.  

Steps to Set Up Google Search Tool  
1. Set the environment variables GOOGLE_API_KEY and GOOGLE_CSE_ID.  
2. Refer to the official guide or documentation for instructions on how to acquire these credentials. """

import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

load_dotenv()


google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

# initialize llm with temperature=0 for precise answer
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

# define the google search wrapper tool
search = GoogleSearchAPIWrapper(
    google_api_key=google_api_key,
    google_cse_id=google_cse_id
)


"""The Tool object represents a specific capability or function the system can use. In this case, it's a tool for performing Google searches.

It is initialized with three parameters:

name parameter: This is a string that serves as a unique identifier for the tool. In this case, the name of the tool is "google-search.”
func parameter: This parameter is assigned the function that the tool will execute when called. In this case, it's the run method of the search object, which presumably performs a Google search.
description parameter: This is a string that briefly explains what the tool does. The description explains that this tool is helpful when you need to use Google to answer questions about current events."""

tools = [
    Tool(
        name="google-search",
        func=search.run,
        description="useful for when you need to search google to answer questions about current events",
    ),
]

# create an agent that uses our google search tool
"""Next, we create an agent that uses our Google Search tool:

initialize_agent(): This function call creates and initializes an agent. An agent is a component that determines which actions to take based on user input. These actions can be using a tool, returning a response to the user, or something else.
tools:  represents the list of Tool objects that the agent can use.
agent="zero-shot-react-description": The "zero-shot-react-description" type of an Agent uses the ReAct framework to decide which tool to use based only on the tool's description.
verbose=True: when set to True, it will cause the Agent to print more detailed information about what it's doing. This is useful for debugging and understanding what's happening under the hood.
max_iterations=6: sets a limit on the number of iterations the Agent can perform before stopping. It's a way of preventing the agent from running indefinitely in some cases, which may have unwanted monetary costs."""


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations = 3
)

# run the agent with a query about the Mars rover
response = agent.run("What is the latest news about the Mars rover?")
print(response)