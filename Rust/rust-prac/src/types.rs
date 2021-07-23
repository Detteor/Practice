pub fn run() {
    // By default this is i32
    let x = 1;
    // Default is f64
    let y = 2.5;
    //Add Exp Type
    let z: i64 = 4545454545;
    //Find max size
    println!("Max i32: {}", std::i32::MAX);
    println!("Max i64: {}", std::i64::MAX);

    // Bool
    let is_active: bool = true;

    //Get bool expression
    let is_greater: bool = 10>5;

    //char
    let a1 = 'a';
    let face = '\u{1F600}';

    println!("{:?}", (x,y,z,is_active, is_greater, a1, face));
}