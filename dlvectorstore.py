"""
Deep Lake provides storage for embeddings and their corresponding metadata in the context of LLM apps. It enables hybrid searches on these embeddings and their attributes for efficient data retrieval. It also integrates with LangChain, facilitating the development and deployment of applications.

Deep Lake provides several advantages over the typical vector store:

It’s multimodal, which means that it can be used to store items of diverse modalities, such as texts, images, audio, and video, along with their vector representations. 
It’s serverless, which means that we can create and manage cloud datasets without creating and managing a database instance. This aspect gives a great speedup to new projects.
Last, it’s possible to easily create a data loader out of the data loaded into a Deep Lake dataset. It is convenient for fine-tuning machine learning models using common frameworks like PyTorch and TensorFlow."""

# Import necessary libraries
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType


load_dotenv()  
openai_api_key = os.getenv("OPENAI_API_KEY")
activeloop_token = os.getenv("ACTIVELOOP_TOKEN")

# intiatilize the llm and embedding models
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# create our documents
texts = [
    "Napoleon Bonaparte was born in August 1769",
    "Louis XIV was born in September 1638",
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

docs = text_splitter.create_documents(texts)

# create deeplake dataset
my_activeloop_org_id = "naeemaziz"
my_activeloop_dataset_name = "langchain_course_from_zero_to_hero"
dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"
db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

# add documents to the dataset
db.add_documents(docs)     

# create a retrievalQA chain
retrieval_qa = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
)

# create an agent that uses the retrievalQA chain as a tool

tools = [
    Tool(
        name = "Retrieval QA System",
        func=retrieval_qa.run,
        description = "Useful for answering questions based on the documents stored in the DeepLake dataset"
    ),
]

agent = initialize_agent(
    tools, 
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

response = agent.run("When was Napoleon Bonaparte born?")
print(response)

"""This example demonstrates how to use Deep Lake as a vector database and create an agent with a RetrievalQA chain as a tool to answer questions based on the given document.

Let’s add an example of reloading an existing vector store and adding more data.

We first reload an existing vector store from Deep Lake that's located at a specified dataset path. Then, we load new textual data and split it into manageable chunks. Finally, we add these chunks to the existing dataset, creating and storing corresponding embeddings for each added text segment:"""

# load an existing deeplake dataset and specify embedding function
db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

# create new docuemnts
new_texts = [
    "Albert Einstein was born in March 1879",
    "Isaac Newton was born in January 1643",
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.create_documents(new_texts)

# add new documents to the dataset
db.add_documents(docs)

# we then create a new agent and ask a question that can be answered only by the last documents added 
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

# create a retiriever from the db
retrieval_qa = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
)

# instantiate a tool that uses the retriever
tools = [
    Tool(
        name = "Retrieval QA System",
        func=retrieval_qa.run,
        description = "Useful for answering questions based on the documents stored in the DeepLake dataset"
    ),
]

agent = initialize_agent(
    tools, 
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

response = agent.run("When was Isaac Newton born?")
print(response)

#The LLM successfully retrieves accurate information by using the power of Deep Lake as a vector store and the OpenAI language model.
