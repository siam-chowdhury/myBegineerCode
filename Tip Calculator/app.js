


var bill_amount, service_percent, amount_people;
    

var get_data = () => {    
    bill_amount = document.querySelector("#billAmount").value;
    service_percent = document.querySelector("#Option").value;
    amount_people = document.querySelector("#pplAmount").value;
    
    calculate_tip(bill_amount, service_percent, amount_people);
}


var calculate_tip = (bill_amount, service_percent, amount_people) => {

    var tip, fianl_tip;
    var service = parseInt(service_percent);
    service /= 100;

    if (amount_people == 0) {
        amount_people = 1;
    }
    
    tip = (bill_amount*service)/amount_people;    
    fianl_tip = parseFloat(tip).toFixed(2);
    document.querySelector("#tip").innerHTML = fianl_tip;

    


}
