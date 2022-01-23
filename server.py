from flask import Flask, render_template, session, request, redirect, flash

from model import connect_to_db, db
import helper

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def function():
    return render_template("homepage.html")

@app.route("/screener")
def display_screener():

    return render_template("screener.html")

@app.route("/screener/<question_id>")
def display_screener_question(question_id):
    """Render question based on question ID."""

    return render_template(f"screener_{question_id}.html")

@app.route("/processing", methods=["POST"])
def process_form_to_db():
    """Write form answers to db"""

    tracker = int(request.form.get("tracker"))

    if tracker == 0:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user_exist = helper.get_user_by_email(email)

        if user_exist:
            flash ("This email is already registered on our website. Please log in.")
            return redirect ("/")
        else:
            user = helper.create_user(email, password, name)
            db.session.add(user)
            db.session.commit()
            flash ("Account created.")
            return redirect("/screener/1")
    elif tracker ==2:
        pass

    

@app.route("/screener-calculations", methods=["POST"])
def calculate_cut_offs():
    fruit_days = request.form.get("fruit_days")
    fruit_days = int(fruit_days)
    fruit_qty = request.form.get("fruit_qty")
    fruit_qty = int(fruit_qty)
    veg_days = request.form.get("veg_days")
    veg_days = int(veg_days)
    veg_qty = request.form.get("veg_qty")
    veg_qty = int(veg_qty)
    rmeat_days = request.form.get("rmeat_days")
    rmeat_days = int(rmeat_days)
    rmeat_qty = request.form.get("rmeat_qty")
    rmeat_qty = int(rmeat_qty)
    pmeat_days = request.form.get("pmeat_days")
    pmeat_days = int(pmeat_days)
    pmeat_qty = request.form.get("pmeat_qty")
    pmeat_qty = int(pmeat_qty)
    rgrains_days = request.form.get("rgrains_days")
    rgrains_days = int(rgrains_days)
    rgrains_qty = request.form.get("rgrains_qty")
    rgrains_qty = int(rgrains_qty)
    wgrains_days = request.form.get("wgrains_days")
    wgrains_days = int(wgrains_days)
    wgrains_qty = request.form.get("wgrains_qty")
    wgrains_qty = int(wgrains_qty)

    daily_fruit_intake = fruit_days * fruit_qty / 7
    daily_veg_intake = veg_days * veg_qty / 7
    daily_fv_intake = daily_fruit_intake + daily_veg_intake

    weekly_rmeat_intake = rmeat_days * rmeat_qty
    weekly_pmeat_intake = pmeat_days * pmeat_qty
    weekly_red_pro_meat_intake = weekly_rmeat_intake + weekly_pmeat_intake

    daily_rgrains_intake = rgrains_days * rgrains_qty / 7
    daily_wgrains_intake = wgrains_days * wgrains_qty / 7
    daily_grain_ratio = daily_wgrains_intake / daily_rgrains_intake

    diet_rec = fruit_veg = red_pro_meat = whole_grains = True
    
    if daily_fv_intake >= 5:
        fruit_veg = False
    
    if weekly_red_pro_meat_intake <3:
        red_pro_meat = False
    
    if daily_grain_ratio >=1:
        whole_grains = False

    return ("Calculated")

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
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)