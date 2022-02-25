"""Module 3 Quiz Functions"""
from flask import Flask, session
from model import db, User, Module, Score, connect_to_db
from datetime import datetime

import json

import helper



def post_score(score):
    """Receive score as json.
        Post to database."""
   
    timestamp = helper.create_timestamp()
    user_id = session['user_id']
    module_id = 3
    new_score_record = helper.set_score(timestamp, user_id, module_id, score)
    db.session.add(new_score_record)
    db.session.commit()
    
    #Check if completed date exists for module assignment.
    #If not, set timestamp
    assignment = helper.get_assigned_module(user_id, module_id)

    if assignment.completion_date is None:
        assignment.completion_date = timestamp
    
    db.session.add(assignment)
    db.session.commit()

    return 'score posted'

 




