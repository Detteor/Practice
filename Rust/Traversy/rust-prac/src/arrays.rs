//Fixed list where the elements are the same data types

pub fn run() {
    use std::mem::size_of_val;
    let number: [i32; 5] = [1,2,3,4,5];

    let mut numbers: [i32; 5] = [1,2,3,4,5];

    //re-assign values
    numbers[2] = 20;
    //replace value in an array
    println!("{:?}", numbers);
    //Access single value in the array
    println!("Single Value: {}", number[0]);
    //get length of the array
    println!("Array Length: {}", numbers.len());
    //Array are stack allocated
    println!("Array occupies {} bytes", size_of_val(&numbers));
    //get slice
    let slice: &[i32] = &number[0..2];
    println!("Slice: {:?}", slice);
}