import os
os.environ["OPENAI_API_KEY"] = "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"


from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


llm = OpenAI(openai_api_key="OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful shirts"))