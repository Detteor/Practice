// Prim str = immutable
// String = growable, use when you need to mod or own string data

pub fn run(){
    //immutable string
    let hello = "hello";
    //growable String
    let hell = String::from("Hello");
    //mutable String
    let mut hella = String::from("Hello ");

    //Get length of strings
    println!("Length: {} and {}", hello.len(), hell.len());
    //Will push character to the end of the string by default, used with chars
    hella.push('W');
    //Push more than one character to the string
    hella.push_str("yoyo");

    //cap in bytes
    println!("Capacity: {}", hella.capacity());
    //check if String Empty
    println!("Is Empty: {}", hella.is_empty());
    //contains substring
    println!("Contain 'yoyo': {}", hella.contains("yoyo"));
    //replace string
    println!("Replace: {}", hella.replace("yoyo", "yaya"));
    //String Loop
    //for loop example
    for word in hella.split_whitespace(){
        println!("{}", word);
    }
    //Create string with capacity
    let mut s = String::with_capacity(10);
    s.push('a');
    s.push('b');
    println!("{}", s);
    //Assertion Testing, only an error if fails
    assert_eq!(2, s.len());
    assert_eq!(10, s.capacity());

    println!("{} and {} and {}", hello, hell, hella);
}