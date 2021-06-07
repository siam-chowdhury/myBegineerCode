
var num;
var letters = [];


// get input number, what user add
function storeInput() {
    var userInput = document.getElementById("frm1");
    num = userInput.elements[0].value;
    var check = (num >= 8 && num <= 20) ? makePWD(num) : alert("Password must be contain 8-20 letters");
}


// add char [A-Z] [a-z] and special symbol
function add_words() {
    for (var i = 65; i <= 122; i++) {
        var ch = String.fromCharCode(i);
        letters.push(ch);
    }
}





// store random index char
var final = "";
function makePWD(num) {

    var cnt = 0;
    add_words();
    for (var i = 0; i < num; i++) {
        var rand = Math.floor(Math.random() * letters.length);
        final += letters[rand];
    }
    document.getElementById("demo").innerHTML = "Your password is : " + final;
    final = "";
}

