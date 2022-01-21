"""Helper functions."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_module(name, description):
    """Create and return a new module."""

    module = Module(name=name, description=description)

    return module

