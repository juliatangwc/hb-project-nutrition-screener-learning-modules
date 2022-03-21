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
                document.querySelector('#fooditems').insertAdjacentHTML ('beforeend', 
                `<div class="cards" id="item${question}" draggable="true" ondragstart="dragstart_handler(event)">
                ${questions[question]}</div>`)
            };
    });

//Add functions for drag and drop
function dragstart_handler(ev) {
    // Add the target element's id to the data transfer object
    ev.dataTransfer.setData("text", ev.target.id);
    // ev.dataTransfer.setData("text/html", ev.target.outerHTML);
    ev.dataTransfer.dropEffect = "move";
  }

function dragover_handler(ev) {
    ev.preventDefault();
    ev.dataTransfer.dropEffect = "move";
   }
function drop_handler(ev, ele) {
    ev.preventDefault();
    // Get the id of the target and add the moved element to the target's DOM
    const data = ev.dataTransfer.getData("text");
    ele.appendChild(document.getElementById(data));
   }

// Post request for sending answers and getting results 

const button = document.querySelector('#submit-button');
   

button.addEventListener('click', evt => {
    evt.preventDefault();

    if (button.innerHTML === 'Submit'){

        console.log('current button: submit')
        
        button.innerHTML = 'Try again';

        const wgrains = document.querySelector('#wgrains');
        const rgrains = document.querySelector('#rgrains');

        const q = (id) => (document.querySelector(id));

        const wGrainList = [];
        const rGrainList = [];

        for (let i = 1; i < 13; i++) {
            wgrains.contains(q(`#item${i}`))? wGrainList.push(i):null;
            rgrains.contains(q(`#item${i}`))? rGrainList.push(i):null;
        };
        
        console.log(wGrainList);
        console.log(rGrainList);

        const formInputs = {
            'wgrains': wGrainList,
            'rgrains': rGrainList
        };

        console.log(formInputs);
    
        fetch('/wholegrains-quiz', {
            method:'POST',
            body: JSON.stringify(formInputs),
            headers:{
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.querySelector('#score-display').innerHTML = `Your score is ${data['score']}/4.`;
            document.querySelector('#correct-answers').innerHTML = data['answers']; 
        });
    }else{
        button.innerHTML = 'Submit';
        
        fetch('/wholegrains-quiz')
        .then(response => response.json())
        .then(data => {
            const questions = data;
            document.querySelector('#score-display').innerHTML = '';
            document.querySelector('#correct-answers').innerHTML = '';
            document.querySelector('#fooditems').innerHTML = '<h5>Food Items</h5> ';
            document.querySelector('#wgrains').innerHTML = '<h5>Whole Grains</h5>';
            document.querySelector('#rgrains').innerHTML = '<h5>Refined Grains</h5>';
            for (const question in questions) {
                document.querySelector('#fooditems').insertAdjacentHTML ('beforeend', `<div class="cards" id="item${question}" draggable="true" ondragstart="dragstart_handler(event)">${questions[question]}</div>`)
            };
        });
    };
});

// Example of how to grab child elements starting with the same words
// window.addEventListener('DOMContentLoaded', () => {

//     //Get elements under fooditems div with id starting with item
//     const matches = [];
//     const elements = document.getElementById("fooditems").children;
//     for(var i = 0; i < elements.length; i++) {
//         if(elements[i].id.indexOf('item') == 0) {
//             matches.push(elements[i]);
//         }
//     }
//     //For matching elements, add them to ondragstart event listener
//     for (const match in matches){
//         match.addEventListener("dragstart", dragstart_handler);
//     }
//   });
