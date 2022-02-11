'use strict';

//Module 1 Quiz
//Fill in the blanks
//A total of 10 possible questions (currently hard coded as dictionary in m1_dietrec.py)
//Randomize to show 3 each time (generate_question in m1_dietrec.py)
//Submit button
//On submit, send post request to route
//Server will do answer check and post score to db
//Display score and correct answers
//Try again button


fetch('/dietrec-quiz')
    .then(response => response.json())
    .then(data => {
            const questions = data;
            for (const question in questions) {
                document.querySelector('#question-box').insertAdjacentHTML ('beforeend', `<li>${questions[question]}</li>`)
            };
    });

