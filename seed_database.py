"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import helper
import model
import server

os.system("dropdb diet-screener")
os.system('createdb diet-screener')

model.connect_to_db(server.app)
model.db.create_all()

# Load module data from JSON file
with open('data/modules.json') as f:
    module_data = json.loads(f.read())


for module in module_data:
    # Get the name and description from the module dictionary.
    name = module['name']
    description = module['description']
    
    # Create a module
    new_module= helper.create_module(name, description)

    # Add module to database
    model.db.session.add(new_module)

model.db.session.commit()

#Create 10 test users
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'
    name = f'User{n}'

    user = helper.create_user(email, password, name)
    model.db.session.add(user)

model.db.session.commit()
    