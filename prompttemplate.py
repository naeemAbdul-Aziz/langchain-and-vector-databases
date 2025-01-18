from langchain_core.prompts.prompt import PromptTemplate

template = """Question: {question}


Answer: """

prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

question = "what is the capital city of france?"

