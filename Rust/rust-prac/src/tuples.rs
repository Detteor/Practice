//Tuples group together values of diff types
//Max 12 Elements
pub fn run() {
    let person: (&str, &str, i8) = ("Mark", "Texas", 36);

    println!("{} is from {} and is {} years old", person.0, person.1, person.2);
}