"""Helper functions."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, connect_to_db

def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)

    return user

def create_module(name, description):
    """Create and return a new module."""

    module = Module(name=name, description=description)

    return module

def get_user_by_email(email):
    """Check if user with email exists.
        If true, return user. 
        If false, return None."""
    
    return User.query.filter(User.email == email).first()
