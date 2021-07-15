// use ferris_says::say;
// use std::io::{stdout, BufWriter};
// mod print;
// mod vars;
// mod types;
// mod string;
// mod tuples;
// mod arrays;
// mod vectors;
// mod conditionals;
// mod loops;
mod functions;

fn main() {
    functions::run();
    // conditionals::of_age();
    // println!("Hello World!");
    // let stdout = stdout();
    // let message = String::from("Hello Fellow Rustaceans!");
    // let width = message.chars().count();

    // let mut writer = BufWriter::new(stdout.lock());
    // say(message.as_bytes(), width, &mut writer).unwrap();
}
