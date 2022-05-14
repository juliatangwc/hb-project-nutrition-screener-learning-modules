"""Helper functions."""

from model import db, User, Screener, Progress, ModuleAssignment, Module, Score, connect_to_db
from datetime import datetime




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

def get_assigned_module(user_id, module_id):

    assignment = ModuleAssignment.query.filter(ModuleAssignment.user_id==user_id, ModuleAssignment.module_id==module_id).first()

    return assignment



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
