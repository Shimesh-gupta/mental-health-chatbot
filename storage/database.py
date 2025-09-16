import os
import json

class Database:
    def __init__(self, db_path="chat_history.json"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                json.dump([], f)

    def save_message(self, user_message, bot_response):
        with open(self.db_path, "r") as f:
            history = json.load(f)
        history.append({"user": user_message, "bot": bot_response})
        with open(self.db_path, "w") as f:
            json.dump(history, f)
