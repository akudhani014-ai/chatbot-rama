from flask import Flask, render_template, request, jsonify
from core import get_bot_reply

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"reply": "Pesan kosong"}), 400

        reply = get_bot_reply(user_message)
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
