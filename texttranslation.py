from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # Deprecated, but keeping for this example

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Define the translation prompt template
translation_template = "Please translate '{text}' from {source_language} to {target_language}."
translation_prompt = PromptTemplate(
    input_variables=["source_language", "target_language", "text"],
    template=translation_template,
)

# Create the translation chain
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

# Define input values as a single dictionary
input_data = {
    "source_language": "English",
    "target_language": "French",
    "text": "Your text here",
}

# Invoke the chain and get the translation
translated_text = translation_chain.invoke(input_data)

# Print the result
print(translated_text)
