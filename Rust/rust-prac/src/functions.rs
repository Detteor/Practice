pub fn run() {
    greeting("Hello", "Mark");
}

fn greeting(greet: &str, name: &str) {
    println!("{} {}, nice to meet you", greet, name);

}