import json


def load_db():
    with open("games_db.json") as f:
        return json.load(f)


db = load_db()
