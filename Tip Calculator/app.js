


var bill_amount, service_percent, amount_people
    

var get_data = () => {    
    bill_amount = document.querySelector("#billAmount").value;
    service_percent = document.querySelector("#Option").value;
    amount_people = document.querySelector("#pplAmount").value;
    
    // calculate_tip(bill_amount, service_percent, amount_people);

    var service = parseInt(service_percent);
    service /= 100;

    var tip = (bill_amount*service)/amount_people;
    var fianl_tip = parseFloat(tip).toFixed(2);
    document.querySelector("#tip").innerHTML = fianl_tip;




}


// var calculate_tip = (bill_amount, service_percent, amount_people) => {

//     alert(service_percent)


// }

// calculate_tip()