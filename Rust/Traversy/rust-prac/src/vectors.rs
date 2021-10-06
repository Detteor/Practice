//Vectors - resizable Vectors

pub fn run(){
    use std::mem::size_of_val;
    let mut numbers: Vec<i32> = vec![1,2,3,4];

    //re-assign values
    numbers[2] = 20;
    //replace value in an Vector
    println!("{:?}", numbers);
    //Access single value in the Vector
    println!("Single Value: {}", numbers[0]);
    //get length of the Vector
    println!("Vector Length: {}", numbers.len());
    //Vector are stack allocated
    println!("Vector occupies {} bytes", size_of_val(&numbers));
    //get slice
    let slice: &[i32] = &numbers[0..2];
    println!("Slice: {:?}", slice);
    //add value to vector
    numbers.push(6);
    numbers.push(5);
    //pop last value in the vector
    numbers.pop();
    println!("{:?}", numbers);
    //for loop vector values
    for n in numbers.iter(){
        println!("Number {}", n);
    }
    //for loop to mutate
    for x in numbers.iter_mut(){
        *x *= 2;
    }
    println!("Numbers Vec: {:?}", numbers);

}