from flask import Flask, request, jsonify
from starter_code import model

app = Flask(__name__)

@app.post("/")
def challengeSetup():
    req_data = request.get_json()
    words = req_data['words']
    strikes = req_data['strikes']
    isOneAway = req_data['isOneAway']
    correctGroups = req_data['correctGroups']
    previousGuesses = req_data['previousGuesses']
    error = req_data['error']

    guess, endTurn = model(words, strikes, isOneAway, correctGroups, previousGuesses, error)

    # Ensure JSON response format
    return jsonify({"guess": guess, "endTurn": endTurn})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
