
import os
os.environ["OPENAI_API_KEY"] = "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"


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


llm = OpenAI(openai_api_key="OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

#print(prompt.format(product="colorful shoes"))
print(llm(prompt.format(product="colorful shoes")))