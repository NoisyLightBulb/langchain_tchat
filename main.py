from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

#import environment variables
load_dotenv()

#initialize ChatOpenAI
chat = ChatOpenAI()

#chat prompt template
prompt = ChatPromptTemplate(
    input_variables = ["content"],
    messages = [
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)


#create chain
chain = LLMChain(
    llm = chat,
    prompt = prompt
)

content = ""
while content != "exit":
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
