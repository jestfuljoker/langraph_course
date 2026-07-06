# `init_chat_model` allow us to create an instance of chat model
# without specify the provider class
from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model("google_genai:gemini-2.5-flash")

response = llm.invoke("Hello, how's it going?")

print(response)
