from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

#import environment variables
load_dotenv()

#initialize ChatOpenAI
chat = ChatOpenAI()

#initialize chat memory
memory = ConversationBufferMemory(
    chat_memory = FileChatMessageHistory("messages.json"),          #storing message history across sessions
    memory_key = "messages",
    return_messages = True
    )

#chat prompt template
prompt = ChatPromptTemplate(
    input_variables = ["content", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),              #chat history
        HumanMessagePromptTemplate.from_template("{content}")]
)


#create chain
chain = LLMChain(
    llm = chat,
    prompt = prompt,
    memory = memory
)

content = ""
while content != "exit":
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
