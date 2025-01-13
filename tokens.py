from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

text = "what would be a good company name for a company that builds rag agents for university students to help them summarixe their slides and textbooks? as well as help them answer questions about the content of their slides and textbooks?"

print(llm(text))

