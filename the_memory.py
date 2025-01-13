"""In LangChain, Memory refers to the mechanism that stores and manages the conversation history between a user and the AI. It helps maintain context and coherency throughout the interaction, enabling the AI to generate more relevant and accurate responses. Memory, such as ConversationBufferMemory, acts as a wrapper around ChatMessageHistory, extracting the messages and providing them to the chain for better context-aware generation."""


from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory())

# Start the conversation
conversation.predict(input="tell me about yourself")

# Continue the conversation
conversation.predict(input="what do you do for fun?")
conversation.predict(input="what is your favorite movie?")

print(conversation)
