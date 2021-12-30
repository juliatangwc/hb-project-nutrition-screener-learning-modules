from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

@app.route("/")
def function():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)