const foodList = {  1: {'code':1,'name':'chicken','img':'/static/img/protein-quiz/chicken.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of chicken because it is a white meat.'},
                    2: {'code':2,'name':'salmon','img':'static/img/protein-quiz/salmon.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of salmon because it is a fish.'},
                    3: {'code':3,'name':'shrimp','img':'static/img/protein-quiz/shrimp.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of shrimp because it is a seafood.'},
                    4: {'code':4,'name':'beef','img':'static/img/protein-quiz/beef.jpg','correct':true,'correctAnswer':'You should limit the intake of beef because it is a red meat.'},
                    5: {'code':5,'name':'pork','img':'static/img/protein-quiz/pork.jpg','correct':true,'correctAnswer':'You should limit the intake of pork because it is a red meat.'},
                    6: {'code':6,'name':'lamb','img':'static/img/protein-quiz/lamb.jpg','correct':true,'correctAnswer':'You should limit the intake of lamb because it is a red meat.'},
                    7: {'code':7,'name':'tofu','img':'static/img/protein-quiz/tofu.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of tofu because it is a plant-based protein.'},
                    8: {'code':8,'name':'bacon','img':'static/img/protein-quiz/bacon.jpg','correct':true,'correctAnswer':'You should limit the intake of bacon because it is a processed meat.'},
                    9: {'code':9,'name':'sausage','img':'static/img/protein-quiz/sausage.jpg','correct':true,'correctAnswer':'You should limit the intake of sausage because it is a processed meat.'},
                    10: {'code':10,'name':'lentils','img':'static/img/protein-quiz/lentils.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of lentils because it is a plant-based protein.'},
                    11: {'code':11,'name':'eggs','img':'static/img/protein-quiz/eggs.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of eggs.'},
                    12: {'code':12,'name':'milk','img':'static/img/protein-quiz/milk.jpg','correct':false,'correctAnswer':'You do not have to limit the intake of milk.'}
                }

const Quiz = () => {

    // Generate a list of 4 random number
    let nums = new Set();
    while (nums.size !== 4) {
        const num = Math.floor(Math.random() * (Object.keys(foodList).length +1));
        if (num !== 0){
            nums.add(num);
        };
    };

    //Selected answer state to keep track of selections
    //Pass to individual food as prop
    //When a food component is clicked on, the code will be added to set at parent(quiz) level

    const [selectedAnswers,setSelectedAnswer] = React.useState(new Set())
    const [display, setDisplay] = React.useState(false);
    const [score, setScore] = React.useState(null);
    const [correctAnswerDivs, setCorrectAnswerDivs] = React.useState([]);

    const setSelectedAnswers = (childData) => {
        if (selectedAnswers.has(childData)){
            selectedAnswers.delete(childData)
            console.log(selectedAnswers, 'selectedAnswers')
        } else {
            selectedAnswers.add(childData)
            console.log(selectedAnswers, 'selectedAnswers')
        }
    };

    // Empty list to hold all food item divs
    const foodItemDivs = [];

    // For each number, use info in object to initialize a foodList div
    for(const num of nums){
        const foodObj = foodList[num]
        console.log(foodObj, 'foodObj')
        console.log(num)
        foodItemDivs.push(
            <FoodItem {...foodObj} setSelectedAnswers={setSelectedAnswers} />
        ) 
    };

    //Button to submit score to server and write to database
    //Show scores and answers when clicked

    const handleSubmit = () => {
        let TempScore = 0;
        const wrongList = [];
        
        for(const num of nums){
            if (foodList[num]['correct'] && selectedAnswers.has(num)){
                TempScore += 1;
            } else if (foodList[num]['correct'] === false && selectedAnswers.has(num) === false){
                TempScore += 1;
            } else if (foodList[num]['correct'] && selectedAnswers.has(num)===false){
                wrongList.push(num);
            } else if (foodList[num]['correct'] === false && selectedAnswers.has(num)){
                wrongList.push(num);
            }
        };

        setScore(TempScore);

        console.log(score, 'score');
        console.log(wrongList, 'wrongList')
        
        fetch('/protein-quiz', {
            method: 'POST',
            body: JSON.stringify(score),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.text())
        .then(data => console.log(data));

        setDisplay(true);

        let answerDivs = [];

        for(const wrong in wrongList){
            const answer = foodList[wrong]['correctAnswer'];
            console.log(answer, 'answer')
            answerDivs.push(
            <Answer correctAnswer={answer}/>
            ) 
        };

        setCorrectAnswerDivs(answerDivs)

    }
    
    return(
        <div className="quiz-wrapper">
            <Score score={score} display={display ? 'block' : 'none'} />
            {foodItemDivs}
            <br></br>
            {correctAnswerDivs}
            <br></br>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    )
}

const FoodItem = (props) => {
    const { code, name, img, correct, correctAnswer, setSelectedAnswers } = props;

    const white = '#FFFFFF';
    const gray = '#D3D3D3';

    const [color, setColor] = React.useState(white);
    
    const handleClickColor = () => {
        const newColor = color === white ? gray : white;
        setColor(newColor);
    }

    return(
        <div className="food-item" id={code} onClick={() => {handleClickColor(); setSelectedAnswers(code);}} style={{ backgroundColor: color }}>
            <img className="food-img" src={img}/>
            <h5>{name}</h5>
        </div>
    )
};

const Answer = (props) => {
    const {correctAnswer} = props;

    return(
        <div className="answer">
            <p>{correctAnswer}</p>
        </div>
    )
}

const Score = (props) => {
    const {score, display} = props;

    return(
        <div className="score" style={{ 'display': display }}>
            <p>Your score is {score}/4.</p>
        </div>
    )
}

ReactDOM.render(<Quiz />, document.querySelector('#root'));
