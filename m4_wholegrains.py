"""Module 4 Quiz Functions"""
from flask import Flask, session
from model import db, User, Module, Score, connect_to_db
from datetime import datetime
from random import sample

import json

import helper

module4_food_items = {
    1 : '<p>White rice</p>',
    2 : '<p>Brown rice</p>',
    3 : '<p>Quinoa</p>',
    4 : '<p>Millet</p>',
    5 : '<p>Oatmeal</p>',
    6 : '<p>Regular pasta</p>',
    7 : '<p>Whole wheat pasta</p>',
    8 : '<p>White bread</p>',
    9 : '<p>Rice noodles</p>',
    10 : '<p>Egg noodles</p>',
    11 : '<p>Soba noodles</p>',
    12 : '<p>Popcorn</p>'
}

module4_answer_key = {
    1 : 'rgrains',
    2 : 'wgrains',
    3 : 'wgrains',
    4 : 'wgrains',
    5 : 'wgrains',
    6 : 'rgrains',
    7 : 'wgrains',
    8 : 'rgrains',
    9 : 'rgrains',
    10 : 'rgrains',
    11 : 'wgrains',
    12 : 'wgrains'
}

module1_correct_answers = {
    1 : 'White rice is a refined grain.',
    2 : 'Brown rice is a whole grain.',
    3 : 'Quinoa is a whole grain.',
    4 : 'Millet is a whole grain.',
    5 : 'Oatmeal is a whole grain.',
    6 : 'Regular pasta is a refined grain.',
    7 : 'Whole wheat pasta is a whole grain.',
    8 : 'White bread is a refined grain.',
    9 : 'Rice noodle is a refined grain.',
    10 : 'Egg noodle is a refined grain.',
    11 : 'Soba noodle is a whole grain.',
    12 : 'Popcorn is a whole grain.'
}

def generate_questions():
    """Randomly choose 4 food items out of food item dictionary.
        Return json with html of the 4 questions."""
    
    questions = {}
    numbers = sample(range(1,13), 4)
    
    for n in numbers:
        questions[n] = module4_food_items[n]
    
    return json.dumps(questions)

# def check_answers(answers):
#     """Receive input as json.
#         Check answers against answer key.
#         Return responses based on correctness of answers."""
#     #Set score to 0
#     score = 0

#     #Check answers. Return correct answer if answer is incorrect. 
#     #If question was not assigned, answer will be None.
#     #Correct answer will increase score by 1. 
#     for answer in answers:
#         if answers[answer] != None:
#             if answers[answer] in module1_answer_key[answer]:
#                 answers[answer] = "<p class='correct-answer'>Correct!</p>"
#                 score += 1
#             else:
#                 answers[answer] = f"<p class='wrong-answer'>Incorrect! <br> The correct answer is: {module1_correct_answers[answer]} </p>"
    
#     #Write score to db
#     answers['score'] = score
#     timestamp = helper.create_timestamp()
#     user_id = session['user_id']
#     module_id = 1
#     new_score_record = helper.set_score(timestamp, user_id, module_id, score)
#     db.session.add(new_score_record)
#     db.session.commit()
    
#     #Check if completed date exists for module assignment.
#     #If not, set timestamp
#     assignment = helper.get_assigned_module(user_id, module_id)

#     if assignment.completion_date is None:
#         assignment.completion_date = timestamp
    
#     db.session.add(assignment)
#     db.session.commit()

#     return json.dumps(answers)

 




