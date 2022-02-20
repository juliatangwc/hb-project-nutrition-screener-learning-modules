const foodList = {  '1': {'name':'chicken','img':'/static/img/protein-quiz/chicken.jpg','correct':'True'},
                    '2': {'name':'salmon','img':'static/img/protein-quiz/salmon.jpg','correct':'True'},
                    '3': {'name':'shrimp','img':'static/img/protein-quiz/shrimp.jpg','correct':'True'},
                    '4': {'name':'beef','img':'static/img/protein-quiz/beef.jpg','correct':'False'},
                    '5': {'name':'pork','img':'static/img/protein-quiz/pork.jpg','correct':'False'},
                    '6': {'name':'lamb','img':'static/img/protein-quiz/lamb.jpg','correct':'False'},
                    '7': {'name':'tofu','img':'static/img/protein-quiz/tofu.jpg','correct':'True'},
                    '8': {'name':'bacon','img':'static/img/protein-quiz/bacon.jpg','correct':'False'},
                    '9': {'name':'sausage','img':'static/img/protein-quiz/sausage.jpg','correct':'False'},
                    '10': {'name':'lentils','img':'static/img/protein-quiz/lentils.jpg','correct':'True'},
                    '11': {'name':'eggs','img':'static/img/protein-quiz/eggs.jpg','correct':'True'},
                    '12': {'name':'milk','img':'static/img/protein-quiz/milk.jpg','correct':'True'}
                }

const Quiz = props => {
    // Generate a list of 5 random number
    const nums = new Set();
    while(nums.size !== 5) {
        nums.add(Math.floor(Math.random() * foodList.length));
    }
    // For each number, use info in object to initialize a foodList div
    for(const num of nums){
        const info = foodList[num]
        <FoodItem info={info}/>
    }

    return(
        <div className="quiz-wrapper">
            <FoodItem />
            <FoodItem />
            <FoodItem />
        </div>
    )
}

const FoodItem = props => {
    const { code, name, img, correct } = props;
    const [display, setDisplay] = React.useState('None');
    
    let numWrong = 0;

    const showAnswer = () => {
        setDisplay = 'Block';
        if ({correct}!=='True'){
            numWong += 1;
        }
    }

    return(
        <div className="food-item" id={code} onClick={showAnswer}>
            <img className="food-img" src={img}/>
            <h5>{name}</h5>
        </div>
    )
};

const Answer = props => {
    const {code, correctAnwer} = props;

    return(<div className="answer" id={code} display={display}>
        <p>{correctAnswer}</p>
    </div>)
}

ReactDOM.render(<Quiz />, document.querySelector('#root'));

