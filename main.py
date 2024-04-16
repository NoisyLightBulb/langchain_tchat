from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import FileChatMessageHistory, ConversationSummaryMemory
from dotenv import load_dotenv

#import environment variables
load_dotenv()

#initialize ChatOpenAI
chat = ChatOpenAI(verbose = True)

#initialize chat memory
memory = ConversationSummaryMemory(
    #chat_memory = FileChatMessageHistory("messages.json"),          #storing message history accross sessions
    memory_key = "messages",
    return_messages = True,
    llm = chat
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
    memory = memory,
    verbose = True
)

content = ""
while content != "exit":
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])
