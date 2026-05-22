from flask import Flask, render_template, request, jsonify
from agents.lead_advisor import lead_advisor

app = Flask(__name__)
conversation_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.json
    user_message = data.get("message", "")
    
    response = lead_advisor(user_message, conversation_history)
    
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": response})
    
    if len(conversation_history) > 20:
        conversation_history = conversation_history[-20:]
    
    return jsonify({"response": response})

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
