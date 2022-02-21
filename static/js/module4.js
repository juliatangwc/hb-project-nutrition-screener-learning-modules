'use strict';

//Module 4 Quiz
//Whole Grains
//Sorting into the correct boxes

//A total of 12 possible items (currently hard coded as dictionary in m4_wholegrains.py)
//Randomize to show 4 each time (generate_question in m4_wholegrains.py)
//Submit button

//On submit, send post request to route
//Server will do answer check and post score to db
//Display score and correct answers
//Try again button

//Fetch request for getting food items
fetch('/wholegrains-quiz')
    .then(response => response.json())
    .then(data => {
            const questions = data;
            for (const question in questions) {
                document.querySelector('#fooditems').insertAdjacentHTML ('beforeend', `<div id="item${question}" draggable="true">${questions[question]}</div>`)
            };
    });

//Add functions for drag and drop
function dragstart_handler(ev) {
    // Add the target element's id to the data transfer object
    ev.dataTransfer.setData("text/plain", ev.target.id);
    ev.dataTransfer.setData("text/html", ev.target.outerHTML);
    ev.dataTransfer.dropEffect = "move";
  }

window.addEventListener('DOMContentLoaded', () => {

    //Get elements under fooditems div with id starting with item
    const matches = [];
    const elements = document.getElementById("fooditems").children;
    for(var i = 0; i < elements.length; i++) {
        if(elements[i].id.indexOf('item') == 0) {
            matches.push(elements[i]);
        }
    }
    //For matching elements, add them to ondragstart event listener
    for (const match in matches){
        match.addEventListener("dragstart", dragstart_handler);
    }
  });

function dragover_handler(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move";
   }
function drop_handler(ev) {
    ev.preventDefault();
    // Get the id of the target and add the moved element to the target's DOM
    const data = ev.dataTransfer.getData("text/html");
    ev.target.appendChild(document.getElementById(data));
   }

   // Post request for sending answers and getting results 
// const quiz = document.querySelector('#dietrec-quiz')
// const button = document.querySelector('#submit-button');
   

// button.addEventListener('click', evt => {
//     evt.preventDefault();

//     if (button.innerHTML === 'Submit'){

//         console.log('current button: submit')
        
//         button.innerHTML = 'Try again';
    
//         const q = (id) => (document.querySelector(id))

//         const formInputs = {
//             1: q('#m1q1') !== null ? q('#m1q1').value : null,
//             2: q('#m1q2') !== null ? q('#m1q2').value : null,
//             3: q('#m1q3') !== null ? q('#m1q3').value : null,
//             4: q('#m1q4') !== null ? q('#m1q4').value : null,
//             5: q('#m1q5') !== null ? q('#m1q5').value : null,
//             6: q('#m1q6') !== null ? q('#m1q6').value : null,
//             7: q('#m1q7') !== null ? q('#m1q7').value : null,
//             8: q('#m1q8') !== null ? q('#m1q8').value : null,
//             9: q('#m1q9') !== null ? q('#m1q9').value : null,
//             10: q('#m1q10') !== null ? q('#m1q10').value : null,
//         };

//         console.log(formInputs);

//         fetch('/dietrec-quiz', {
//             method:'POST',
//             body: JSON.stringify(formInputs),
//             headers:{
//                 'Content-Type': 'application/json',
//             },
//         })
//         .then(response => response.json())
//         .then(data => {
//             console.log(data);
//             document.querySelector('#score-display').innerHTML = `Your score is ${data['score']}/3.`;
//             for (const item in data){
//                 if (data[item] !== null && item !== 'score') {
//                     document.querySelector(`#li${item}`).insertAdjacentHTML ('beforeend', `<br>${data[item]}<br>`)
//                 };
//             };  
//         });
//     }else{
//         button.innerHTML = 'Submit';
        
//         fetch('/dietrec-quiz')
//         .then(response => response.json())
//         .then(data => {
//             const questions = data;
//             document.querySelector('#question-box').innerHTML = '';
//             document.querySelector('#score-display').innerHTML = '';
//             for (const question in questions) {
//                 document.querySelector('#question-box').insertAdjacentHTML ('beforeend', `<li id="li${question}">${questions[question]}</li>`)
//             };
//         });
//     };
// });

