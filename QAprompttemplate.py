from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub

template = """Question: {question}


Answer: """

prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

question = "what is the capital city of france?"



# using hugging face model google/fla-t5-largge to answer the questions
hub_llm = HuggingFaceHub(
        repo_id='google/flan-t5-large',
    model_kwargs={'temperature':0}
)

chain = prompt | hub_llm

# ask the user question about the capital of France
print(chain.invoke(question))

"""An updated version of the class exists in the :class:`~langchain-huggingface package and should be used instead. To use it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:`~langchain_huggingface import HuggingFaceEndpoint``. 
  hub_llm = HuggingFaceHub(

  to make this code future proof:
  from langchain_huggingface import HuggingFaceEndpoint
  hub_llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/google/flan-t5-large",
    huggingfacehub_api_token="your_token_here"
)
  """

# asking multiple questions
llm_chain = LLMChain(llm=hub_llm, prompt=prompt)

qa = [
    {'question': "What is the capital city of France?"},
    {'question': "What is the largest mammal on Earth?"},
    {'question': "Which gas is most abundant in Earth's atmosphere?"},
    {'question': "What color is a ripe banana?"}
]


res = llm_chain.generate(qa)
print( res )

"""The warning you received indicates that LLMChain is deprecated in LangChain 0.1.17 and will be removed in version 1.0. You are encouraged to switch to the new approach using RunnableSequence, such as prompt | llm.

For your code, the refactor would look like this:

from langchain.prompts import PromptTemplate
from langchain.llms import YourLLM  # Replace with the appropriate LLM
from langchain.runnables import RunnableSequence

# Define your prompt template
prompt = PromptTemplate(input_variables=["input"], template="Your prompt here with {input}")

# Use RunnableSequence
hub_llm = YourLLM()  # Initialize your LLM here
runnable = prompt | hub_llm

# Now you can run the sequence
response = runnable.invoke({"input": "example input"})
print(response)"""


multi_template = """Answer the following questions one at a time.

Questions:
{questions}

Answers:
"""
long_prompt = PromptTemplate(template=multi_template, input_variables=["questions"])


llm_chain = long_prompt | hub_llm


qs_str = (
    "What is the capital city of France?\n" +
    "What is the largest mammal on Earth?\n" +
    "Which gas is most abundant in Earth's atmosphere?\n" +
		"What color is a ripe banana?\n"
)

llm_chain.invoke(qs_str)

"""
caution

c:\Users\naeemaziz\Desktop\activeloop\langchain-and-vdb\QAprompttemplate.py:20: LangChainDeprecationWarning: The class `HuggingFaceHub` was deprecated in LangChain 0.0.21 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-huggingface package and should be used instead. To use it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:`~langchain_huggingface import HuggingFaceEndpoint``. 
  hub_llm = HuggingFaceHub(
Paris
c:\Users\naeemaziz\Desktop\activeloop\langchain-and-vdb\QAprompttemplate.py:42: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.       
  llm_chain = LLMChain(llm=hub_llm, prompt=prompt)
generations=[[Generation(text='paris')], [Generation(text='giraffe')], [Generation(text='nitrogen')], [Generation(text='yellow')]] llm_output=None run=[RunInfo(run_id=UUID('b6c80a1a-c874-41e6-a597-d9a34e61d959')), RunInfo(run_id=UUID('e9fbf220-badf-4258-aa23-e40a3a3ffa71')), RunInfo(run_id=UUID('84718792-202f-4863-9c7f-cf3ba6d7adc6')), RunInfo(run_id=UUID('d14d3115-237e-41ec-8f37-77c1936d44e9'))] type='LLMResult'
PS C:\Users\naeemaziz\Desktop\activeloop\langchain-and-vdb> """