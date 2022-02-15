"""Module 1 Quiz Functions"""
from flask import Flask, session
from model import db, User, Module, Score, connect_to_db
from datetime import datetime
from random import sample

import json

import helper

module1_questions = {
    1 : '<p>A healthy lifestyle <input type="text" class="answer-box" id="m1q1"> (can/cannot) lower the risk of cancer.</p>',
    2 : '<p>There are <input type="text" class="answer-box" id="m1q2"> special food that can prevent cancer.</p>',
    3 : '<p>Every day, I should consume at least <input type="text" class="answer-box" id="m1q3"> servings of fruit and vegetables.</p>',
    4 : '<p>One serving of vegetable is <input type="text" class="answer-box" id="m1q4"> bowl of raw vegetables or half a bowl of cooked vegetables.</p>',
    5 : '<p>I should choose <input type="text" class="answer-box" id="m1q5"> grain products like brown rice over refined grain products like white rice.</p>',
    6 : '<p>I should not eat too much <input type="text" class="answer-box" id="m1q6">, such as pork, beef and lamb.</p>',
    7 : '<p>Choosing poultry, fish, or <input type="text" class="answer-box" id="m1q7">-based protein such as tofu is a good idea.</p>',
    8 : '<p>I ought to avoid <input type="text" class="answer-box" id="m1q8"> meat like sausages and ham.</p>',
    9 : '<p>Drinks like soda and lemonade contain added <input type="text" class="answer-box" id="m1q9">, which means they are empty calories (not providing nutrients).</p>',
    10 : '<p>Drinking plenty of <input type="text" class="answer-box" id="m1q10"> (at least 8 cups per day) will help keep me healthy.</p>'
}

module1_answer_key = {
    1 : ['can'],
    2 : ['no'],
    3 : ['5','five'],
    4 : ['1','one'],
    5 : ['whole'],
    6 : ['red meat'],
    7 : ['plant'],
    8 : ['processed'],
    9 : ['sugar'],
    10 : ['water']
}

module1_correct_answers = {
    1 : 'A healthy lifestyle can lower the risk of cancer.',
    2 : 'There are no special food that can prevent cancer.',
    3 : 'Every day, I should consume at least 5 servings of fruit and vegetables.',
    4 : 'One serving of vegetable is one bowl of raw vegetables or half a bowl of cooked vegetables.',
    5 : 'I should choose whole grain products like brown rice over refined grain products like white rice.',
    6 : 'I should not eat too much red meat, such as pork, beef and lamb.',
    7 : 'Choosing poultry, fish, or plant-based protein such as tofu is a good idea.',
    8 : 'I ought to avoid processed meat like sausages and ham.',
    9 : 'Drinks like soda and lemonade contain added sugar, which means they are empty calories (not providing nutrients).',
    10 : 'Drinking plenty of water (at least 8 cups per day) will help keep me healthy.'
}

def generate_questions():
    """Randomly choose 3 questions out of question dictionary.
        Return json with html of the 3 questions."""
    
    questions = {}
    numbers = sample(range(1,11), 3)
    
    for n in numbers:
        questions[n] = module1_questions[n]
    
    return json.dumps(questions)

def check_answers(answers):
    """Receive input as json.
        Check answers against answer key.
        Return responses based on correctness of answers."""
    #Set score to 0
    score = 0

    #Check answers. Return correct answer if answer is incorrect. 
    #If question was not assigned, answer will be None.
    #Correct answer will increase score by 1. 
    for answer in answers:
        if answers[answer] != None:
            if answers[answer] in module1_answer_key[answer]:
                answers[answer] = "<p class='correct-answer'>Correct!</p>"
                score += 1
            else:
                answers[answer] = f"<p class='wrong-answer'>Incorrect! <br> The correct answer is: {module1_correct_answers[answer]} </p>"
    
    #Write score to db
    answers['score'] = score
    timestamp = helper.create_timestamp()
    user_id = session['user_id']
    module_id = 1
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

    return json.dumps(answers)

 




