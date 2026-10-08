
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature = 0.8,
    max_tokens = 300
)

prompt = input("user input :")
response = llm.invoke(prompt)
print(response.content)