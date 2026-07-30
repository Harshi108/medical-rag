from flask import Flask, request, jsonify
from flask_cors import CORS
from retrieval import retrieve_answer

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return " Medical AI Backend Running"

@app.route("/ask",methods = ["POST"])
def ask():
    data = request.get_json()
    question = data.get("question","")
    answer = retrieve_answer(question)

    return jsonify({
        "answer":f"you asked: {question}"
    })

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()
    question = data.get("question", "")

    answer = retrieve_answer(question)

    return jsonify({
        "answer": answer
    })
if __name__ == "__main__":
    app.run(debug = True)