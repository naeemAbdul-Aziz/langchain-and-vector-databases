"""
In LangChain, a chain is an end-to-end wrapper around multiple individual components, providing a way to accomplish a common use case by combining these components in a specific sequence. The most commonly used type of chain is the LLMChain, which consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser.

The LLMChain works as follows:

Takes (multiple) input variables.
Uses the PromptTemplate to format the input variables into a prompt.
Passes the formatted prompt to the model (LLM or ChatModel).
If an output parser is provided, it uses the OutputParser to parse the output of the LLM into a final format.
In the next example, we demonstrate how to create a chain that generates a possible name for a company that produces eco-friendly water bottles. By using LangChain's LLMChain, PromptTemplate, and OpenAIclasses, we can easily define our prompt, set the input variables, and generate creative outputs.
"""

from langchain.prompts import  PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

prompt = PromptTemplate(input_variables=["product"], template="Generate a possible name for a company that produces {product}.")

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(product="eco-friendly water bottles"))
