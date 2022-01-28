"""Functions to process screener."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, connect_to_db

def process_form(tracker):

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
            now = datetime.now()
            timestamp = now.strftime("%Y/%m/%d %H:%M:%S")

            #Define and set screener tracker to 1
            screener_tracker = 1

            #Create a new progress tracker
            progress = helper.create_progress_tracker(screener_id, timestamp, screener_tracker)
            db.session.add(progress)
            db.session.commit()
            
            flash (f"Account created.")
            return redirect("/screener/1")
    
    elif tracker == 1:
        #Update screener database with form data
        screener_id = session['screener_id']
        veg_days = request.form.get("veg_days")
        screener = helper.update_screener_q1(screener_id, veg_days)
        db.session.add(screener)
        
        #Update progress tracker
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
        screener_tracker = 2
        progress = helper.update_progress(screener_id,timestamp,screener_tracker)
        db.session.add(progress)

        #Write to database
        db.session.commit()

        #Redirect to next question
        return redirect("/screener/2")

    elif tracker == 2:
        #Update screener
        screener_id = session['screener_id']
        veg_qty = request.form.get("veg_qty")
        screener = helper.update_screener_q2(screener_id, veg_qty)
        db.session.add(screener)
        
        #Update progress tracker
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
        screener_tracker = 3
        progress = helper.update_progress(screener_id,timestamp,screener_tracker)
        db.session.add(progress)

        #Write to database
        db.session.commit()

        #Redirect to next question
        return redirect("/screener/3")