from flask import Flask, render_template, request, jsonify
from models.chatbot import Chatbot
from storage.database import Database

app = Flask(__name__)
chatbot = Chatbot()
db = Database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = chatbot.respond(user_message)
    db.save_message(user_message, bot_response)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)