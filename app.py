from flask import Flask
from flask import redirect, render_template, request, session
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", same_name=None)


@app.route("/try", methods=["GET", "POST"])
def try_password():
    if request.method == "POST":
        password = request.form["password"]
        if test_if_ok(password):
            return render_template("index.html", same_name=True)
        return render_template("index.html", same_name=False)


def test_if_ok(word):
    print(len(word))
    if len(word) >= 8:
        return True
