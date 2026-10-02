from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()


llm=ChatGroq(
    model="openai/gpt-oss-20b"
)

print("My first chatbot")

history=[]

while True:

# prompt="what is python ?"
    prompt=input("Enter your prompt:")
    history.append(prompt)
    if prompt == "Exit":
        break

    responce=llm.invoke(history)
    history.append(AIMessage(content=responce.content))
    print(responce.content)

    # print(history)