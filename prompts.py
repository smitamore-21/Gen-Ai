from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=300
)

prompt_template = PromptTemplate.from_template(
    """Analyse the {topic} and give me a structured 3 lines theory about it , dont guess it, answer should be in a one paragraph"""

)

prompt = prompt_template.invoke(
    {"topic" : input("User input :")}
)

reasponce = llm.invoke(prompt)
print(reasponce.content)