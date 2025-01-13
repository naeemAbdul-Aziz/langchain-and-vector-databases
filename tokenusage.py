
# tracking token usage
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback


llm = ChatOpenAI(model_name="gpt-4o-mini", n=2)

with get_openai_callback() as cb:
    result = llm.invoke("Tell me a joke")
    print(cb)