from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from rich import print

llm = init_chat_model("google_genai:gemini-2.5-flash")

# At various times, we want to make the model behaviour in a certain way.
# For that we can use a special type of message that should not be exhibited for the final user
system_message = SystemMessage(
    "You are a study guide who helps students learn new topics. \n\n"
    "Your job is to guide the student's ideas so that they can understand their "
    "chosen topic without receiving ready-made answers from you. \n\n"
    "Avoid talking about subjects parallel to the chosen topic. If the student "
    "does not provide a topic initially, your first job will be to request a "
    "topic until the student tells you. \n\n"
    "You can be friendly, cool, and caring And treat the student like a teenager. "
    "We want to avoid fatigue of a rigid study and maintain the engagement in what it's studying."
    "The next messages will be from a student."
)

# When someone sends messages to the model, this message will be converted
# into a `HumanMessage` that will have the specific format so the model knows how to distinguish
# what is a system message, what is a user message, and what is a message from the model answering
# to the user.
human_message = HumanMessage("Hello, my name is Chriszão!")

# We must send a list of messages to the model with the history of the chat.
# If we don't do that, every message will be treated as the first message received by the model
# and it won't know anything about the previous messages.
messages = [system_message, human_message]

response = llm.invoke(messages)

print(f"{'AI':-^80}")
print(response.content)

messages.append(response)

# Here we are simulating a simple chat just to understand some concepts. When using LangGraph
# this won't be necessary.
while True:
    print(f"{'Human':-^80}")
    user_input = input("Enter your message: ")
    human_message = HumanMessage(user_input)

    if user_input.lower() in ["exit", "quit", "bye", "q"]:
        break

    messages.append(human_message)

    response = llm.invoke(messages)

    print(f"{'AI':-^80}")
    print(response.content)
    print()

    messages.append(response)

print()
print(f"{'Histórico':-^80}")
print(*[f"{m.type.upper()}\n{m.content}\n\n" for m in messages], sep="", end="")
print()
