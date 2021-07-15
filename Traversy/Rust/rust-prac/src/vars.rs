pub fn run() {
    // Variables are immutable by Default
    let name = "Mark";
    let mut age = 36;
    println!("My name is {} and I am {}", name, age);
    age = 37;
    println!("My name is {} and I am {}", name, age);

    //Define Constant
    const ID: i32 = 001;
    println!("ID: {}", ID);

    //Assign multiple Vars
    let ( my_name, my_age) = ("Mark", 36);
    println!("{} is {}", my_name, my_age);
}