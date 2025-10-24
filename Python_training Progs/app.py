from flask import Flask, render_template, request
import hangman_art  # 👈 your hangman art file

app = Flask(__name__)

# A simple game state (in-memory)
WORD = "pumpkin"
guessed_letters = ['_'] * len(WORD)
false_chances = 6

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_letters, false_chances

    message = ""
    if request.method == "POST":
        user_input = request.form["letter"].lower()

        if user_input in WORD:
            for idx, letter in enumerate(WORD):
                if letter == user_input:
                    guessed_letters[idx] = user_input
            message = "✅ Correct!"
        else:
            false_chances -= 1
            message = f"❌ Wrong! Chances left: {false_chances}"

    current_word = ' '.join(guessed_letters)
    hangman_stage = art.stages[6 - false_chances]  # assuming you have stages list in art.py

    return render_template("index.html",
                           current_word=current_word,
                           hangman=hangman_stage,
                           message=message)
