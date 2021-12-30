from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

@app.route("/")
def function():
    return render_template("homepage.html")

@app.route("/screener")
def display_screener():
    return render_template("screener.html")

@app.route("/login")
def user_login():
    return render_template("login.html")

@app.route("/dashboard")
def show_screener():
    # return render_template("dashboard.html")
    pass

@app.route("/dietrec")
def show_dietary_recs():
    # return render_template("dietrec.html")
    pass

@app.route("/fruitveg")
def show_fruit_veg_info():
    # return render_template("fruitveg.html")
    pass

@app.route("/redmeat")
def show_red_meat_info():
    # return render_template("redmeat.html")
    pass

@app.route("/wholegrain")
def show_whole_grain_info():
    # return render_template("wholegrain.html")
    pass



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)