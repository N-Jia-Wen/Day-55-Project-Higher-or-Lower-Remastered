from flask import Flask
import random


CORRECT_NUM = random.randint(0, 9)
TOO_LOW_IMG = ("https://media.giphy.com/media/lp6kwhyO1prr2/giphy.gif?"
               "cid=790b7611m28sni493znw7ghz8081qgaow4ubhyrr52dzz3f4&ep=v1_gifs_search&rid=giphy.gif&ct=g")
TOO_HIGH_IMG = ("https://media.giphy.com/media/QVsIdgs7sToek/giphy.gif?cid=ecf05e47yit20dflc3b6y6dp8ssrmt4bluhmt0fj"
                "2qc63xn1&ep=v1_gifs_search&rid=giphy.gif&ct=g")
JUST_RIGHT_IMG = ("https://media.giphy.com/media/jVEPGJEn9gT269bDCo/giphy.gif?cid=ecf05e47bep8ng5nxkaij5sh9nbjseelz35"
                  "egvbr38gp4ikv&ep=v1_gifs_search&rid=giphy.gif&ct=g")

app = Flask(__name__)


@app.route("/")
def home():
    return ("<h1>Welcome to the Higher Or Lower Game!</h1>"
            "<h2>Guess a number between 0 to 9 and type '/' followed by your answer into your search bar.</h2>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:number>")
def check_answer(number: int):
    if number < CORRECT_NUM:
        return (f"<h1 style='color: red'>Too low, try again!</h1>"
                f"<img src='{TOO_LOW_IMG}'>")
    elif number > CORRECT_NUM:
        return (f"<h1 style='color: blue'>Too high, try again!</h1>"
                f"<img src='{TOO_HIGH_IMG}'>")
    else:
        return (f"<h1 style='color: purple'>Congrats! You found me!</h1>"
                f"<img src='{JUST_RIGHT_IMG}'>")


if __name__ == "__main__":
    app.run()
