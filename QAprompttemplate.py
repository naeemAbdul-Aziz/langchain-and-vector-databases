from langchain_core.prompts.prompt import PromptTemplate

template = """Question: {question}


Answer: """

prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

question = "what is the capital city of france?"



# using hugging face model google/fla-t5-largge to answer the questions
from langchain.chains import LLMChain
from langchain import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="google/flax-t5-large",
     model_kwargs = {'temperature' : 0}
       )

chain = prompt | hub_llm

print(chain(question))