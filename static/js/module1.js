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

//Fetch request for getting quiz questions
fetch('/dietrec-quiz')
    .then(response => response.json())
    .then(data => {
            const questions = data;
            for (const question in questions) {
                document.querySelector('#question-box').insertAdjacentHTML ('beforeend', `<li id=${question}>${questions[question]}</li>`)
            };
    });

//Post request for sending answers and getting results 
const quiz = document.querySelector('#dietrec-quiz')

quiz.addEventListener('submit', evt => {
    evt.preventDefault();

    const q = (id) => (document.querySelector(id))

    const formInputs = {
        1: q('#m1q1') !== null ? q('#m1q1').value : null,
        2: q('#m1q2') !== null ? q('#m1q2').value : null,
        3: q('#m1q3') !== null ? q('#m1q3').value : null,
        4: q('#m1q4') !== null ? q('#m1q4').value : null,
        5: q('#m1q5') !== null ? q('#m1q5').value : null,
        6: q('#m1q6') !== null ? q('#m1q6').value : null,
        7: q('#m1q7') !== null ? q('#m1q7').value : null,
        8: q('#m1q8') !== null ? q('#m1q8').value : null,
        9: q('#m1q9') !== null ? q('#m1q9').value : null,
        10: q('#m1q10') !== null ? q('#m1q10').value : null,
    };

    console.log(formInputs);

    fetch('/dietrec-quiz', {
        method:'POST',
        body: JSON.stringify(formInputs),
        headers:{
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        for (const item in data){
            if (data[item] !== null) {
                document.querySelector(`#${item}`).insertAdjacentHTML ('beforeend', `<br>${data[item]}`)
            };
        };  
    })
        // document.querySelector('#question-box').insertAdjacentHTML ('beforeend', data)
        //if it is not null, then put it under the answer box.
        // for (const item in data){
        //     if (data[item] !== null) {
        //         document.querySelector(`${item}`).insertAdjacentHTML ('beforeend', `<br>${data[item]}`)
        //     };
        // };
});



