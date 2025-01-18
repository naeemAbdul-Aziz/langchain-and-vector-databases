from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Define the translation prompt template
translation_template = "Translate the following text from {source_language} to {target_language}: {text}"
translation_prompt = PromptTemplate(
    input_variables=["source_language", "target_language", "text"],
    template=translation_template,
)

# Combine prompt and LLM using RunnableSequence
translation_chain = translation_prompt | llm

# Define input values as a single dictionary
input_data = {
    "source_language": "English",
    "target_language": "French",
    "text": "Hello, how are you?",
}

# Invoke the chain and get the translation
translated_text = translation_chain.invoke(input_data)

# Print the result
print(translated_text)
