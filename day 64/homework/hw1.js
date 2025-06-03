function hobby(){
    let hobby = prompt('what is your favorite hobby')
    alert('you favorite hobby is' + hobby)
}

function Fullname(){
    let name = prompt('what is your name?: ');
    let surname = prompt('what is your surname?: ');
    let fullname = name + "" + surname;
    alert(fullname)
}

function colorchanger(){
    let colors = prompt('Enter your color: ')
    document.getElementById('text').textContent = colors
}

function emoji(){
    let emoji = prompt("your favorite emoji here: ")
    alert('Hello' + emoji)
}

function title(){
    let titles = prompt('what do u want title to be?')
    document.title = titles
}


function inputer(){
    let value = document.getElementById('textinput').value
    alert('You entered'  + value)
}

function background(){
    let color = document.getElementById('backgrounds').value;
    document.body.style.backgroundColor = color;
}


function fullnames(){
    let name = document.getElementById('name').value;
    let surname = document.getElementById('surname').value;
    let fullname = name + '' + surname;
    document.getElementById('Fullname').textContent = fullname
}