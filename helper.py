"""Helper functions."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, connect_to_db
from datetime import datetime

def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)

    return user

def get_user_by_email(email):
    """Check if user with email exists.
        If true, return user. 
        If false, return None."""
    
    return User.query.filter(User.email == email).first()

def check_user_password(email, password):
    """If password entered matches password in databse, return True.
        If password does not  match, return False."""
    
    user = User.query.filter(User.email == email).first()

    if user.password == password:
        return user.user_id
    else:
        return False

def get_user_by_id(user_id):
    """Return a user object by user ID."""
    
    return User.query.get(user_id)
    
def get_most_updated_screener_id(user_id):
    """Find all screeners done by user by user ID. Return the most updated screener ID."""
    screeners = Screener.query.filter_by(user_id=user_id).all()
    most_updated = 0

    for screener in screeners:
        if screener.screener_id > most_updated:
            most_updated = screener.screener_id
    
    return most_updated

def create_module(name, description, href, img):
    """Create and return a new module."""

    module = Module(name=name, description=description, href=href, img=img)

    return module

def create_initial_screener(user_id):
    """Create and return a new screener object."""

    screener = Screener(user_id=user_id)

    return screener

def update_screener_q1(screener_id, veg_days):
    """Update answer to Q1 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q1_veg_days = veg_days

    return screener

def update_screener_q2(screener_id, veg_qty):
    """Update answer to Q2 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q2_veg_qty = veg_qty

    return screener

def update_screener_q3(screener_id, fruit_days):
    """Update answer to Q3 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q3_fruit_days = fruit_days

    return screener

def update_screener_q4(screener_id, fruit_qty):
    """Update answer to Q4 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q4_fruit_qty = fruit_qty

    return screener

def update_screener_q5(screener_id, rmeat_days):
    """Update answer to Q5 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q5_rmeat_days = rmeat_days

    return screener

def update_screener_q6(screener_id, rmeat_qty):
    """Update answer to Q6 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q6_rmeat_qty = rmeat_qty

    return screener

def update_screener_q7(screener_id, pmeat_days):
    """Update answer to Q7 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q7_pmeat_days = pmeat_days

    return screener

def update_screener_q8(screener_id, pmeat_qty):
    """Update answer to Q8 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q8_pmeat_qty = pmeat_qty

    return screener

def update_screener_q9(screener_id, wgrains_days):
    """Update answer to Q9 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q9_wgrains_days = wgrains_days

    return screener

def update_screener_q10(screener_id, wgrains_qty):
    """Update answer to Q10 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q10_wgrains_qty = wgrains_qty

    return screener

def update_screener_q11(screener_id, rgrains_days):
    """Update answer to Q11 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q11_rgrains_days = rgrains_days

    return screener

def update_screener_q12(screener_id, rgrains_qty):
    """Update answer to Q12 to database. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.q12_rgrains_qty = rgrains_qty

    return screener

def mark_screener_completion(screener_id, completed_on):
    """Update screeners table with completion timestamp. Return screener object."""
    screener = Screener.query.get(screener_id)
    screener.completed_on = completed_on

    return screener

def get_screener_by_user_id(user_id):
    """Get screener object given user ID. Return screener object."""

    return Screener.query.filter(Screener.user_id == user_id).first()

def create_progress_tracker(screener_id, timestamp, screener_tracker):
    """Create and return a new progress tracker."""

    tracker = Progress(screener_id=screener_id, timestamp=timestamp, screener_tracker=screener_tracker)

    return tracker

def update_progress(screener_id, timestamp, screener_tracker):
    """Update and return progress tracker."""

    tracker = Progress.query.filter(Progress.screener_id == screener_id).first()
    tracker.timestamp = timestamp
    tracker.screener_tracker = screener_tracker

    return tracker

def get_screener_tracker(screener_id):
    """Find progress tracker by screener ID. Return progress object."""
    
    return Progress.query.filter_by(screener_id=screener_id).first()

def assign_module(assignment_date, user_id, module_id):
    """Assign a module to a user."""

    assignment = ModuleAssignment(assignment_date=assignment_date, user_id=user_id, module_id=module_id)

    return assignment

def get_all_assigned_modules_by_user(user_id):
    """Find all modules assigned to user. Return a list of asssigned modules as objects."""
    
    assigned_modules = []
    assignments = ModuleAssignment.query.filter_by(user_id=user_id)

    for assignment in assignments:
        assigned_modules.append(assignment.module)
    
    return assigned_modules

def create_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
    return timestamp
    
def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False