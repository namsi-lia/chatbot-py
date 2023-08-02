# Importing required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot =ChatBot("chatbot",read_only=False,logic_adapters=["chatterbot.logic.BestMatch"])

list_train_data =[
    "Hi there!",
    "Hello! How are you doing?",
    "Hi",
    "How can I assist you today?",
    "What's your name",
    "My name is Botty,I am a chatbot",
    "Nice to meet you.",
    "Thank You for reaching out.",
    "You're welcome.",
    "Goodbye!",
    "See ya later!",
    "Bye!",
    "Thanks!",
    "That was helpful.",
    "Can we connect on LinkedIn or Twitter?",
]

list_trainer =ListTrainer(bot)
#creating list trainer object
list_trainer.train(list_train_data)

while True:
    user_response =input("User:")
    print("ChatBot:"+ str (bot.get_response(user_response)))