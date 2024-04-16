from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

#import environment variables
load_dotenv()

#chat prompt template
prompt = ChatPromptTemplate(
    input_variables = ["content"],
    messages = [
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)


while True:
    content = input(">> ")

    print(f"You entered: {content}")
