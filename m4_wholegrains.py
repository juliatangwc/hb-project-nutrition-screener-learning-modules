"""Module 4 Quiz Functions"""
from flask import Flask, session
from model import db, User, Module, ModuleAssignment, Score, connect_to_db
from datetime import datetime
from random import sample

import json

import helper

module4_food_items = {
    1 : '<img class="thumb" src="/static/img/wgrains-quiz/white_rice.jpg"><div class="cards-inner">White rice</div>',
    2 : '<img class="thumb" src="/static/img/wgrains-quiz/brown_rice.jpg"><div class="cards-inner">Brown rice</div>',
    3 : '<img class="thumb" src="/static/img/wgrains-quiz/quinoa.jpg"><div class="cards-inner">Quinoa</div>',
    4 : '<img class="thumb" src="/static/img/wgrains-quiz/millet.jpg"><div class="cards-inner">Millet</div>',
    5 : '<img class="thumb" src="/static/img/wgrains-quiz/oatmeal.jpg"><div class="cards-inner">Oatmeal</div>',
    6 : '<img class="thumb" src="/static/img/wgrains-quiz/regular_pasta.jpg"><div class="cards-inner">Regular pasta</div>',
    7 : '<img class="thumb" src="/static/img/wgrains-quiz/whole_wheat_pasta.jpg"><div class="cards-inner">Whole wheat pasta</div>',
    8 : '<img class="thumb" src="/static/img/wgrains-quiz/white_bread.jpg"><div class="cards-inner">White bread</div>',
    9 : '<img class="thumb" src="/static/img/wgrains-quiz/rice_noodles.jpg"><div class="cards-inner">Rice noodles</div>',
    10 : '<img class="thumb" src="/static/img/wgrains-quiz/egg_noodles.jpg"><div class="cards-inner">Egg noodles</div>',
    11 : '<img class="thumb" src="/static/img/wgrains-quiz/soba_noodles.jpg"><div class="cards-inner">Soba noodles</div>',
    12 : '<img class="thumb" src="/static/img/wgrains-quiz/popcorn.jpg"><div class="cards-inner">Popcorn</div>'
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

module4_correct_answers = {
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
        correct_answers.insert(0,'<br><h6>Here are the correct answers:</h6>')
        correct_answers.append('<br>')
    
    answers = '<br>'.join(correct_answers)

    #Write score to db
    timestamp = helper.create_timestamp()
    user_id = session['user_id']
    module_id = 4
    new_score_record = Score.set_score(timestamp, user_id, module_id, score)
    db.session.add(new_score_record)
    db.session.commit()
    
    #Check if completed date exists for module assignment
    #If not, set timestamp
    assignment = ModuleAssignment.get_module_assignment(user_id, module_id)

    if assignment.completion_date is None:
        assignment.completion_date = timestamp
    
    db.session.add(assignment)
    db.session.commit()

    return json.dumps({'score':score, 'answers':answers})

