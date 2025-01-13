"""LangChain provides a variety of tools for agents to interact with the outside world. These tools can be used to create custom agents that perform various tasks, such as searching the web, answering questions, or running Python code. In this section, we will discuss the different tool types available in LangChain and provide examples of creating and using them.

In our example, two tools are being defined for use within a LangChain agent: a Google Search tool and a Language Model tool acting specifically as a text summarizer. The Google Search tool, using the GoogleSearchAPIWrapper, will handle queries that involve finding recent event information. The Language Model tool leverages the capabilities of a language model to summarize texts. These tools are designed to be used interchangeably by the agent, depending on the nature of the user's query."""

import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

# instantiate a llmchain specifically for text sumaarization
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
prompt = PromptTemplate(
    input_variables=["query"],
    template="Summarize the following text: {query}"
)

summarize_chain = LLMChain(llm=llm, prompt=prompt)

#tools that our agent will use
#google search via api
search = GoogleSearchAPIWrapper(
    google_api_key=google_api_key,
    google_cse_id=google_cse_id
)

tools = [
    Tool(
        name="search",
        func=search.run,
        description="useful for finding information about current events",
    ),
    Tool(
        name="summerizer",
        func=summarize_chain.run,
        description="useful for summarizing texts",
    )
]

#create our agent that leverages the two tools
agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

response = agent("What is the latest news about the mars rover?")
print(response['output'])

"""
Notice how the agents used at first the “Search” tool to look for recent information about the Mars rover and then used the “Summarizer” tool for writing a summary.

LangChain provides an expansive toolkit that integrates various functions to improve the functionality of conversational agents. Here are some examples:

SerpAPI: This tool is an interface for the SerpAPI search engine, allowing the agent to perform robust online searches to pull in relevant data for a conversation or task.
PythonREPLTool: This unique tool enables the writing and execution of Python code within an agent. This opens up a wide range of possibilities for advanced computations and interactions within the conversation.
If you wish to add more specialized capabilities to your LangChain conversational agent, the platform offers the flexibility to create custom tools. By following the general tool creation guidelines provided in the LangChain documentation, you can develop tools tailored to the specific needs of your application."""