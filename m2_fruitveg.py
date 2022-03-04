"""Module 2 Quiz Functions"""
from flask import Flask, session
from model import db, User, Module, Score, connect_to_db
from datetime import datetime
from random import sample

import json

import helper

module2_food_items = {
    1 : {'name':'Cooked spinach',
        'img':'/static/img/fruitveg-quiz/cooked_spinach.jpg',
        'answer':'Half a cup'},
    2 : {'name':'Baby spinach salad',
        'img':'/static/img/fruitveg-quiz/spinach_salad.jpg',
        'answer':'One cereal bowl'},
    3 : {'name':'Apple',
        'img':'/static/img/fruitveg-quiz/apple.jpg',
        'answer':'One medium'},
    4 : {'name':'Blueberries',
        'img':'/static/img/fruitveg-quiz/blueberries.jpg',
        'answer':'One cup'},
    5 : {'name':'Grapes',
        'img':'/static/img/fruitveg-quiz/grapes.jpg',
        'answer':'One cup'},
    6 : {'name':'Tomato',
        'img':'/static/img/fruitveg-quiz/tomato.jpg',
        'answer':'One medium'},
    7 : {'name':'Baby carrots',
        'img':'/static/img/fruitveg-quiz/baby_carrots.jpg',
        'answer':'One cup (7-10 pcs)'},
    8 : {'name':'Cooked carrots',
        'img':'/static/img/fruitveg-quiz/cooked_carrots.jpg',
        'answer':'One cup'},
    9 : {'name':'Broccoli florets',
        'img':'/static/img/fruitveg-quiz/broccoli.jpg',
        'answer':'About 5 pieces'},
    10 : {'name':'Mushrooms',
        'img':'/static/img/fruitveg-quiz/mushrooms.jpg',
        'answer':'One cup'}
}

module2_correct_answers = {
    1 : 'A serving of cooked spinach is half a cup.',
    2 : 'A serving of baby spinach salad is one cereal bowl.',
    3 : 'A serving of apple is one medium sized apple.',
    4 : 'A serving of blueberries is one cup, which may contain 30-60 pieces depending on size.',
    5 : 'A serving of grapes is one cup, wich may contain 10-20 grapes depending on size.',
    6 : 'A serving of tomato is one medium sized tomato (not cherry tomatoes).',
    7 : 'A serving of baby carrots is one cup or about 7-10 pieces.',
    8 : 'A serving of cooked carrots is one cup.',
    9 : 'A serving of broccoli florets is about 5 pieces',
    10 : 'A serving of mushrooms is one cup.'
}

def generate_questions():
    """Randomly choose 3 food items out of food item dictionary.
        Return json with html of the 3 questions."""
    
    questions = {}
    numbers = sample(range(1,11), 3)
    
    for n in numbers:
        questions[n] = module2_food_items[n]
    
    return json.dumps(questions)

def check_answers(data):
    """Receive input as json with two lists (wgrains, rgrains) containing item numbers.
        Check answers against answer key.
        Return score and correct answers to be displayed."""
    
    #Set score to 0
    score = 0
    correct_answers = []

    #Check answers by going through the two lists
    #Loop through wgrains list
    #If module4_answer_key[item] is 'wgrains', it is correct: add 1 point
    #Else, it is incorrect, append module4_correct_answers[item] to correct_answers list
    #Loop through rgrains list and do the same
    #Return an object with 'score' and 'answers' (change answer from list to string)

    for item in data['wgrains']:
        if module4_answer_key[item] == 'wgrains':
            score += 1
        else:
            correct_answers.append(module4_correct_answers[item])
    
    for item in data['rgrains']:
        if module4_answer_key[item] == 'rgrains':
            score += 1
        else:
            correct_answers.append(module4_correct_answers[item])

    if correct_answers != []:
        correct_answers.insert(0,'<h6>Here are the correct answers:</h6>')
    
    answers = '<br>'.join(correct_answers)

    #Write score to db
    timestamp = helper.create_timestamp()
    user_id = session['user_id']
    module_id = 4
    new_score_record = helper.set_score(timestamp, user_id, module_id, score)
    db.session.add(new_score_record)
    db.session.commit()
    
    #Check if completed date exists for module assignment
    #If not, set timestamp
    assignment = helper.get_assigned_module(user_id, module_id)

    if assignment.completion_date is None:
        assignment.completion_date = timestamp
    
    db.session.add(assignment)
    db.session.commit()

    return json.dumps({'score':score, 'answers':answers})

