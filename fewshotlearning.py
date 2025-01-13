# Few-shot learning is a remarkable ability that allows LLMs to learn and generalize from limited examples. Prompts serve as the input to these models and play a crucial role in achieving this feature. With LangChain, examples can be hard-coded, but dynamically selecting them often proves more powerful, enabling LLMs to adapt and tackle tasks with minimal training data swiftly.

# This approach involves using the FewShotPromptTemplate class, which takes in a PromptTemplate and a list of a few shot examples. The class formats the prompt template with a few shot examples, which helps the language model generate a better response. We can streamline this process by utilizing LangChain's FewShotPromptTemplate to structure the approach:

from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# Create our examples
examples = [    
    {"query": "What's the weather like?", 
     "answer": "It's raining cats and dogs, better bring an umbrella!"}, 
    {"query": "How old are you?",
     "answer": "Age is just a number, but I'm timeless!"
     },
]

# Create an example template
example_template = """
User: {query}
AI: {answer}
"""

# Create an example prompt
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)

# Break our previous prompt into a prefix and suffix
prefix = """
The following are excerpts from conversations with an AI assistant. The assistant is known for its humor and wit, providing entertaining and amusing responses to users' questions. Here are some examples:
"""

suffix = """
User: {query}
AI:
"""

# Correct the typo: `example_separator` instead of `example_seperator`
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"  # Fixed spelling
)

# Create the chain
chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.0)
chain = few_shot_prompt_template | chat

# Invoke the chain with a query
result = chain.invoke("What's the meaning of life?")
print(result)
