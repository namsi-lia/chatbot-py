# Importing required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot =ChatBot("chatbot",read_only=False,
             logic_adapters=
             [{
                 "import_path:chatterbot.logic.BestMatch"
                 "default_response:Sorry i don't have any response for that"
                 "maximum_similarity_threshold":0.9
               
               
               }])

list_train_data =[
    "Hi there!",
    "Hello! How are you doing?",
    "I'm fine"
    "What's your name",
    "My name is Botty,I am a chatbot",
    "Nice to meet you.",
    "Thank You for reaching out.",
    "You're welcome.",
    "How old are you ?",
    "i'm ageless",
    "Are you male or female? ",
    "No,I am non-binary",
    "What's your job??",
    "I am here to handle all your questions and needs",
    "Great!, What do you want me to help with today?",
    "Help me structure my book",
    "Sure thing boss.",
    "Do you have any specific requirements in mind?",
    "No not yet",
    "i dont know what you are talking about,please clarify??"
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