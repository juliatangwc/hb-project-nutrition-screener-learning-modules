"""Helper functions."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, connect_to_db

def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)

    return user

def get_user_by_email(email):
    """Check if user with email exists.
        If true, return user. 
        If false, return None."""
    
    return User.query.filter(User.email == email).first()

def create_module(name, description):
    """Create and return a new module."""

    module = Module(name=name, description=description)

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
