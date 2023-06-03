
import os
os.environ["OPENAI_API_KEY"] = "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"


from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")
print(output)
