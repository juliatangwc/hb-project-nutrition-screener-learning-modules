'use strict';

//Module 2 Quiz
//Fruit and Vegetables
//Matching

//A total of 10 possible items (currently hard coded as dictionary in m2_fruitveg.py)
//Randomize to show 3 each time (generate_question in m2_wholegrains.py)
//Submit button

//On submit, send post request to route
//Server will do answer check and post score to db
//Display score and correct answers
//Try again button

//Fetch request for getting food items
fetch('/fruitveg-quiz')
    .then(response => response.json())
    .then(data => {
            console.log(data)
            const questions = data;
            for (const question in questions) {
                document.querySelector('#choices').insertAdjacentHTML ('beforeend', 
                `<div id="answer${question}" draggable="true" droppable="false" ondragstart="dragstart_handler(event)">${questions[question]['answer']}</div>`)
                document.querySelector('#fooditems').insertAdjacentHTML ('beforeend', 
                `<div class="food-item-container" id="container${question}">
                    <div class="food-item-box">
                        <img src="${questions[question]['img']}">
                        <br>
                        <p>${questions[question]['name']}</p>
                    </div>
                    <div class="food-item-answer-box" id="drop${question}" ondrop="drop_handler_limit(event,this)" ondragover="dragover_handler(event)"></div>
                </div>`)
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

function drop_handler(ev,ele) {
    console.log(ev.target)
    console.log(ele)
    ev.preventDefault();
    // Get the id of the target and add the moved element to the target's DOM
    const data = ev.dataTransfer.getData("text");
    ele.appendChild(document.getElementById(data));
   }

function drop_handler_limit(ev,ele) {
    ev.preventDefault();
    // Use element to specify where to drop, instead of evt target, which may change
    // Get the id of the target and add the moved element to the target's DOM
    if(ele.children.length === 0){
        const data = ev.dataTransfer.getData("text");
        ele.appendChild(document.getElementById(data));
        };
    }


// Post request for sending answers and getting results 

const button = document.querySelector('#submit-button');
   

button.addEventListener('click', evt => {
    evt.preventDefault();

    if (button.innerHTML === 'Submit'){

        console.log('current button: submit');
        
        button.innerHTML = 'Try again';

        //check which food item divs are on the screen by looking for drop[i]
        //if drop[i] contains choice[i], correct, increment score
        let score = 0;
        const wrong = [];

        const q = (id) => (document.querySelector(id));
        const foodItems = document.querySelector('#fooditems');
        
        for (let i = 1; i < 11; i++) {
            if (foodItems.contains(q(`#drop${i}`))) {
                const dropZone = q(`#drop${i}`);
                if (dropZone.contains(q(`#answer${i}`))){
                    score += 1
                }else{
                    wrong.push(i)
                };
            };
        };
        
        console.log(score);
        console.log(wrong, 'Wrong');

        const formInputs = {
            'score': score,
            'wrong': wrong
        };

        console.log(formInputs, 'formInputs');

        fetch('/fruitveg-quiz', {
            method:'POST',
            body: JSON.stringify(formInputs),
            headers:{
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data, 'Data received');
            document.querySelector('#score-display').innerHTML = `Your score is ${data['score']}/3.`;
            document.querySelector('#correct-answers').innerHTML = data['answers']; 
        });
    }else{
        button.innerHTML = 'Submit';
        
        fetch('/fruitveg-quiz')
        .then(response => response.json())
        .then(data => {

            console.log(data);

            //Reset innerHTMLs
            document.querySelector('#score-display').innerHTML = '';
            document.querySelector('#correct-answers').innerHTML = '';
            document.querySelector('#choices').innerHTML = '<h5>Choices</h5> ';
            document.querySelector('#fooditems').innerHTML = '';
            
            //Refresh questions
            const questions = data;
            
            for (const question in questions) {
                document.querySelector('#choices').insertAdjacentHTML ('beforeend', 
                `<div id="answer${question}" draggable="true" droppable="false" ondragstart="dragstart_handler(event)">${questions[question]['answer']}</div>`);
                document.querySelector('#fooditems').insertAdjacentHTML ('beforeend', 
                `<div class="food-item-container" id="container${question}">
                    <div class="food-item-box">
                        <img src="${questions[question]['img']}">
                        <br>
                        <p>${questions[question]['name']}</p>
                    </div>
                    <div class="food-item-answer-box" id="drop${question}" ondrop="drop_handler_limit(event,this)" ondragover="dragover_handler(event)"></div>
                </div>`);
            };
        });
    };    
});