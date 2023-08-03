# Importing required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template


app =Flask(__name__)

bot = ChatBot("chatbot", read_only=False,
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I don\'t have any response for that.',
                      'maximum_similarity_threshold': 0.9
                  }
              ]
              )


trainer =ChatterBotCorpusTrainer(bot)
#trainer.train('chatterbot.corpus.english')

@app.route("/")
def main():
    return render_template("index.html")



#while True:
    #user_response =input("User:")
    #print("ChatBot:"+ str (bot.get_response(user_response)))

if __name__=="__main__":
    app.run(debug=True)