from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime

from model import connect_to_db, db
import helper

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def function():
    """Show homepage"""
    return render_template("homepage.html")

@app.route("/screener")
def display_screener():
    """Show screener"""

    return render_template("screener.html")

@app.route("/screener/<question_id>")
def display_screener_question(question_id):
    """Render question based on question ID."""

    return render_template(f"screener_{question_id}.html")

@app.route("/processing", methods=["POST"])
def process_form_to_db():
    """Write form answers to db"""

    tracker = int(request.form.get("tracker"))

    # Consider moving this to new file
    # route = processing.process_form(tracker)

    #Question 0: Create user
    if tracker == 0:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user_exist = helper.get_user_by_email(email)

        if user_exist:
            flash ("This email is already registered on our website. Please log in.")
            return redirect ("/")
        else:
            #Create new user and add to database
            user = helper.create_user(email, password, name)
            db.session.add(user)
            db.session.commit()

            #Get user ID of newly created user
            user_id = user.user_id
            session['user_id'] = user_id

            #Start a new screener with user ID and add to database
            screener = helper.create_initial_screener(user_id)
            db.session.add(screener)
            db.session.commit()

            #Get newly created screener ID
            screener_id = screener.screener_id
            session['screener_id'] = screener_id
            
            # Create timestamp
            timestamp = helper.create_timestamp()

            #Define and set screener tracker to 1
            screener_tracker = 1

            #Create a new progress tracker
            progress = helper.create_progress_tracker(screener_id, timestamp, screener_tracker)
            db.session.add(progress)
            db.session.commit()
            
            flash (f"Account created.")
            return redirect("/screener/1")
    
    #Question 1: Veg_days
    elif tracker == 1:
        #Update screener database with form data
        screener_id = session['screener_id']
        veg_days = int(request.form.get("veg_days"))
        screener = helper.update_screener_q1(screener_id, veg_days)
        db.session.add(screener)
        db.session.commit()

        if veg_days == 0:
            #Skip question 2. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 3
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/3")
        else:
            #Redirect to question2. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 2
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/2")

    #Question 2: Veg qty
    elif tracker == 2:
        #Get answers from form
        screener_id = session['screener_id']
        veg_qty = request.form.get("veg_qty")
        #Check if answers are acceptable
        if helper.is_float(veg_qty):
            #Update database with answer
            screener = helper.update_screener_q2(screener_id, veg_qty)
            db.session.add(screener)
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 3
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            #Write to database
            db.session.commit()
            #Redirect to next question
            return redirect("/screener/3")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)

    #Questions 3: Fruit Days  
    elif tracker == 3:
        #Update screener database with form data
        screener_id = session['screener_id']
        fruit_days = int(request.form.get("fruit_days"))
        screener = helper.update_screener_q3(screener_id, fruit_days)
        db.session.add(screener)
        db.session.commit()

        if fruit_days == 0:
            #Skip question 4. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 5
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/5")
        else:
            #Redirect to question 4. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 4
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/4")
    
    #Question 4: Fruit Quantity
    elif tracker == 4:
        #Get answers from form
        screener_id = session['screener_id']
        fruit_qty = request.form.get("fruit_qty")
        #Check if answers are acceptable
        if helper.is_float(fruit_qty):
            #Update database with answer
            screener = helper.update_screener_q4(screener_id, fruit_qty)
            db.session.add(screener)
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 5
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            #Write to database
            db.session.commit()
            #Redirect to next question
            return redirect("/screener/5")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)
    
    #Questions 5: Red Meat Days  
    elif tracker == 5:
        #Update screener database with form data
        screener_id = session['screener_id']
        rmeat_days = int(request.form.get("rmeat_days"))
        screener = helper.update_screener_q5(screener_id, rmeat_days)
        db.session.add(screener)
        db.session.commit()

        if rmeat_days == 0:
            #Skip question 6. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 7
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/7")
        else:
            #Redirect to question 6. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 6
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/6")   
    
    #Question 6: Red Meat Quantity
    elif tracker == 6:
        #Get answers from form
        screener_id = session['screener_id']
        rmeat_qty = request.form.get("rmeat_qty")
        #Check if answers are acceptable
        if helper.is_float(rmeat_qty):
            #Update database with answer
            screener = helper.update_screener_q6(screener_id, rmeat_qty)
            db.session.add(screener)
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 7
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            #Write to database
            db.session.commit()
            #Redirect to next question
            return redirect("/screener/7")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)
    
    #Questions 7: Processed Meat Days  
    elif tracker == 7:
        #Update screener database with form data
        screener_id = session['screener_id']
        pmeat_days = int(request.form.get("pmeat_days"))
        screener = helper.update_screener_q7(screener_id, pmeat_days)
        db.session.add(screener)
        db.session.commit()

        if pmeat_days == 0:
            #Skip question 8. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 9
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/9")
        else:
            #Redirect to question 8. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 8
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/8")   
    
    #Question 8: Processed Meat Quantity
    elif tracker == 8:
        #Get answers from form
        screener_id = session['screener_id']
        pmeat_qty = request.form.get("pmeat_qty")
        #Check if answers are acceptable
        if helper.is_float(pmeat_qty):
            #Update database with answer
            screener = helper.update_screener_q8(screener_id, pmeat_qty)
            db.session.add(screener)
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 9
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            #Write to database
            db.session.commit()
            #Redirect to next question
            return redirect("/screener/9")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)

    #Questions 9: Whole Grains Days
    elif tracker == 9:
        #Update screener database with form data
        screener_id = session['screener_id']
        wgrains_days = int(request.form.get("wgrains_days"))
        screener = helper.update_screener_q9(screener_id, wgrains_days)
        db.session.add(screener)
        db.session.commit()

        if wgrains_days == 0:
            #Skip question 10. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 11
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/11")
        else:
            #Redirect to question 10. Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 10
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/10")   
    
    #Question 10: Whole Grains Quantity
    elif tracker == 10:
        #Get answers from form
        screener_id = session['screener_id']
        wgrains_qty = request.form.get("wgrains_qty")
        #Check if answers are acceptable
        if helper.is_float(wgrains_qty):
            #Update database with answer
            screener = helper.update_screener_q10(screener_id, wgrains_qty)
            db.session.add(screener)
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 11
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            #Write to database
            db.session.commit()
            #Redirect to next question
            return redirect("/screener/11")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)
    #Questions 11: Refined Grains Days
    elif tracker == 11:
        #Update screener database with form data
        screener_id = session['screener_id']
        rgrains_days = int(request.form.get("rgrains_days"))
        screener = helper.update_screener_q11(screener_id, rgrains_days)
        db.session.add(screener)
        db.session.commit()

        if rgrains_days == 0:
            #Skip question 12. Update progress tracker to mark completion. Redirect to do calculations.
            timestamp = helper.create_timestamp()
            screener_tracker = 13
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            screener = helper.mark_screener_completion(screener_id, timestamp)
            db.session.add(screener)
            db.session.commit()
            return redirect("/screener-calculations")
        else:
            #Redirect to question 12. Update progress tracker.
            timestamp = helper.create_timestamp()
            screener_tracker = 12
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            return redirect("/screener/12")   
    
    #Question 12: Refined Grains Quantity
    elif tracker == 12:
        #Get answers from form
        screener_id = session['screener_id']
        rgrains_qty = request.form.get("rgrains_qty")
        #Check if answers are acceptable
        if helper.is_float(rgrains_qty):
            #Update screener database with answer
            screener = helper.update_screener_q12(screener_id, rgrains_qty)
            db.session.add(screener)
            db.session.commit()
            #Update progress tracker
            timestamp = helper.create_timestamp()
            screener_tracker = 13
            progress = helper.update_progress(screener_id,timestamp,screener_tracker)
            db.session.add(progress)
            db.session.commit()
            #Update screener with completion timestamp
            screener = helper.mark_screener_completion(screener_id, timestamp)
            db.session.add(screener)
            db.session.commit()
            #Redirect to calculations
            return redirect("/screener-calculations")
        else:
            flash("Please enter numbers only.")
            return redirect(request.referrer)


@app.route("/screener-calculations", methods=["POST"])
def calculate_cut_offs():
    #Grab screener object that corresponds to user_id
    user_id = session['user_id']
    screener = helper.get_screener_by_user_id(user_id)

    #Assign the variables
    veg_days = screener.q1_veg_days
    veg_qty = screener.q2_veg_qty
    fruit_days = screener.q3_fruit_days
    fruit_qty = screener.q4_fruit_qty
    rmeat_days = screener.q5_rmeat_days
    rmeat_qty = screener.q6_rmeat_qty
    pmeat_days = screener.q7_pmeat_days
    pmeat_qty = screener.q8_pmeat_qty
    wgrains_days = screener.q9_wgrains_days
    wgrains_qty = screener.q10_wgrains_qty
    rgrains_days = screener.q11_rgrains_days
    rgrains_qty = screener.q12_rgrains_qty 

    #Cut-off Calculations
    daily_fruit_intake = fruit_days * fruit_qty / 7
    daily_veg_intake = veg_days * veg_qty / 7
    daily_fv_intake = daily_fruit_intake + daily_veg_intake

    weekly_rmeat_intake = rmeat_days * rmeat_qty
    weekly_pmeat_intake = pmeat_days * pmeat_qty
    weekly_red_pro_meat_intake = weekly_rmeat_intake + weekly_pmeat_intake

    daily_rgrains_intake = rgrains_days * rgrains_qty / 7
    daily_wgrains_intake = wgrains_days * wgrains_qty / 7
    daily_grain_ratio = daily_wgrains_intake / daily_rgrains_intake

    #Create timestamp
    timestamp = helper.create_timestamp()

    #Module assignment
    helper.assign_module(timestamp, user_id, module_id)
    assignment_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    module_id = db.Column(db.Integer, db.ForeignKey("modules.module_id"))
    

    # diet_rec = fruit_veg = red_pro_meat = whole_grains = True
    
    # if daily_fv_intake >= 5:
    #     fruit_veg = False
    
    # if weekly_red_pro_meat_intake <3:
    #     red_pro_meat = False
    
    # if daily_grain_ratio >=1:
    #     whole_grains = False

    #Module assigment to database
    
    return ("Calculated")

@app.route("/login")
def show_login_form():
    """Show form for existing user to log in."""

    return render_template("login.html")

@app.route("/login",methods=["POST"])
def user_login():
    """Existing user log in."""

    email = request.form.get("email")
    password = request.form.get("password")
    
    user_exist = helper.get_user_by_email(email)

    if user_exist:
        checked_user = helper.check_user_password(email, password)
        if checked_user:
            session['user_id'] = checked_user
            flash ("Success! You are logged in!")
        else:
            flash ("Wrong password. Please try again.")
    else:
        flash ("No match for email entered. Please create an account.")
    
    return redirect ("/dashboard")
    

@app.route("/dashboard")
def show_dashboard():
    
    return render_template("dashboard.html")
    
@app.route("/dietrec")
def show_dietary_recs():
    return render_template("dietrec.html")

@app.route("/fruitveg")
def show_fruit_veg_info():
    return render_template("fruitveg.html")

@app.route("/protein")
def show_protein_info():
    return render_template("protein.html")

@app.route("/wholegrains")
def show_whole_grain_info():
    return render_template("wholegrains.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)