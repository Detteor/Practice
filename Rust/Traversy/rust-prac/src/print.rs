pub fn run() {
    //Print to console
    println!("Hello from the print.rs file");

    //Basic Formatting
    println!("{} is from {}", "Mark", "Kinnaman");
    println!("Number: {}", 1);

    //Positional Arguments
    println!("{0} is from {1} likes to {2}", "Mark", "Kinnaman", "code");

    //Named Arguments
    println!("{name} like to play {act}", name = "Mark", act="soccer");

    //Placeholder Traits
    println!("Binary: {:b} Hex: {:x} Octal: {:o}", 10, 10, 10);

    //Placeholder for debug Trait
    println!("{:?}", (12, true, "hello"));

    //Basic Math
    println!("10 + 10 = {}", 10 + 10);
}