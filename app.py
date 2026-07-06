from flask import Flask, jsonify

app = Flask(__name__)

notes = [
    {"id": 1, "title": "Learn Linux"},
    {"id": 2, "title": "Learn Git"},
    {"id": 3, "title": "Learn Docker"}
]

@app.route("/")
def home():
    return jsonify({"message": "Cloud Notes API is running!"})

@app.route("/notes")
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
