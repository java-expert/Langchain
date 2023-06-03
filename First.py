
import os
os.environ["OPENAI_API_KEY"] = "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"


from langchain.llms import OpenAI
llm = OpenAI(openai_api_key="OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))