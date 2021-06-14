

var show_hex_code = document.querySelector("#hex");
var clickButton = document.querySelector("#click");
var bg_color = document.querySelector("#container");


// create random hex code
var generate_random_hexCode = () => {
    var random = Math.floor(Math.random() * 16777216).toString(16);
    return random;
}


// auto click the button : Just for fun
var auto_click = () => {
    setInterval(auto_click, 1000);
    clickButton.click();
}
auto_click()


// change background color
var change_bgColor = () => {
    show_hex_code.innerHTML = "#" + generate_random_hexCode();
    document.body.style.backgroundColor = "#" + generate_random_hexCode();
}





