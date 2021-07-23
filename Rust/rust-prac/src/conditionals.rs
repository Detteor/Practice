//check the conditions
pub fn run(){
    let age: i8= 18;
    let check_id: bool = false;
    //If Else statement
    if age >= 21 && check_id {
        println!("Bartender: What would you like to drink?");
    } else if age < 21 && check_id{
        println!("Bartender: Sorry you have to leave!");
    } else {
        println!("Bartender: I need to see you ID?");
    }

    //Shorthand IF statement
    let is_of_age = if age >=21 { true} else { false };
    println!("Is of Age: {}", is_of_age)
}

pub fn of_age(){
    let age: i8= 18;
    let check_id: bool = false;
    let knows_person_of_age = true;
    //If Else statement
    if age >= 21 && check_id || knows_person_of_age {
        println!("Bartender: What would you like to drink?");
    } else if age < 21 && check_id{
        println!("Bartender: Sorry you have to leave!");
    } else {
        println!("Bartender: I need to see you ID?");
    }
}