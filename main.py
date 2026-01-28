import getpass
import os
from os.path import join, dirname
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
# result1 = model.invoke([HumanMessage(content="Hi! I am Rishabh")])
# print(result1)
# result2=model.invoke([HumanMessage(content="What's my name?")])
# print(result2)

result3 = model.invoke(
    [
        HumanMessage(content="Hi, I am Rishabh"),
        AIMessage(content="Hello Rishabh! How can s help you?"),
        HumanMessage(content="What's my name?")
    ]
)
print(result3)
