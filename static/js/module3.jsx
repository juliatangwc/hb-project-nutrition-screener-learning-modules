const foodList = {  1: {'name':'chicken','img':'/static/img/protein-quiz/chicken.jpg','correct':'True'},
                    2: {'name':'salmon','img':'static/img/protein-quiz/salmon.jpg','correct':'True'},
                    3: {'name':'shrimp','img':'static/img/protein-quiz/shrimp.jpg','correct':'True'},
                    4: {'name':'beef','img':'static/img/protein-quiz/beef.jpg','correct':'False'},
                    5: {'name':'pork','img':'static/img/protein-quiz/pork.jpg','correct':'False'},
                    6: {'name':'lamb','img':'static/img/protein-quiz/lamb.jpg','correct':'False'},
                    7: {'name':'tofu','img':'static/img/protein-quiz/tofu.jpg','correct':'True'},
                    8: {'name':'bacon','img':'static/img/protein-quiz/bacon.jpg','correct':'False'},
                    9: {'name':'sausage','img':'static/img/protein-quiz/sausage.jpg','correct':'False'},
                    10: {'name':'lentils','img':'static/img/protein-quiz/lentils.jpg','correct':'True'},
                    11: {'name':'eggs','img':'static/img/protein-quiz/eggs.jpg','correct':'True'},
                    12: {'name':'milk','img':'static/img/protein-quiz/milk.jpg','correct':'True'}
                }

const Quiz = () => {
    // Generate a list of 5 random number
    let nums = new Set();
    while (nums.size !== 5) {
        const num = Math.floor(Math.random() * (Object.keys(foodList).length +1));
        if (num !== 0){
            nums.add(num);
        };
    };
    
    // Empty list to hold all food item divs
    const foodItemDivs = [];

    // For each number, use info in object to initialize a foodList div
    for(const num of nums){
        const foodObj = foodList[num]
        console.log(foodObj, 'foodObj')
        
        foodItemDivs.push(
            <FoodItem {...foodObj}/>
        ) 
    };

    //Incomplete. Button to submit score to server and write to database
    //Show scores and answers when clicked
    const handleClick = () => {
        fetch('/wholegrains-quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({obj})
        })
        .then(res => res.json())
        .then(data => console.log(data))
    }
    
    return(
        <div className="quiz-wrapper">
            {foodItemDivs}
            <button onClick={handleClick}>Submit</button>
        </div>
    )
}

const FoodItem = (props) => {
    const { name, img, correct } = props;

    const white = '#FFFFFF';
    const lightblue = '#ADD8E6';

    const [color, setColor] = React.useState(white);
    const [display, setDisplay] = React.useState(false);

    
    const setSelected = () => {
        const newColor = color === white ? lightblue : white;
        setColor(newColor);
    }; 

    let numWrong = 0;

    // const showAnswer = () => {
    //     setDisplay(true);
    //     if (correct !== 'True') {
    //         numWrong += 1;
    //     }
    // }

    return(
        <div className="food-item" id={name} onClick={setSelected} style= {{backgroundColor: color}}>
            <img className="food-img" src={img}/>
            <h5>{name}</h5>
            <Answer code={name} correctAnswer={correct} display={display ? 'block' : 'none'}/>
        </div>
    )
};

const Answer = (props) => {
    const {code, correctAnswer, display} = props;

    return(
        <div className="answer" id={code} style={{ 'display': display }}>
            <p>{correctAnswer}</p>
        </div>
    )
}

ReactDOM.render(<Quiz />, document.querySelector('#root'));
