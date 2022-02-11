"""Module 1 Quiz Functions"""

from model import db, User, Module, Score, connect_to_db
from datetime import datetime
from random import choices
import json

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
    10 : '<p>Drinking plenty of <input type="text" class="answer-box" id="m1q10"> (at least 8 cups per day) swill help keep me healthy.</p>'
}

def generate_questions():
    """Randomly choose 3 questions out of question dictionary.
        Return json with html of the 3 questions."""
    
    questions = {}
    numbers = choices(range(1,11), k=3)
    
    for n in numbers:
        questions[n] = module1_questions[n]
    
    return json.dumps(questions)

        




