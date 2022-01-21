function Hello(){
    return(
        <p>Hello World</p>
    )
}

ReactDom.render(<Hello />, document.querySelector('#root'));