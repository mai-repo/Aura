from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('magic.html')

@app.route('/magic-8-ball', methods=['POST'])
def magic_8_ball():
    responses = [
        "Yes - definitely.",
        "It is decidedly so.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    num = random.randint(0, 8)
    question = request.json.get('question', '')

    if not question:
        return jsonify({"error": "Please provide a question"}), 400

    answer = responses[num]
    return jsonify({"question": question, "answer": answer})

if __name__ == '__main__':
    app.run(debug=True)