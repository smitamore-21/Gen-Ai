from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

# chatbot with proper history 

#create one obeject 
llm=ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=200
)

print("My first chatbot")


messages = [
    SystemMessage(content="you are a funny AI assistant, reply in fun way")
]

while True:

    prompt=input("User:")
    messages.append(HumanMessage(content=prompt))
    if prompt == "Exit":
        break

    responce=llm.invoke(messages)
    messages.append(AIMessage(content=responce.content))
    print(responce.content)

    