use std::io::{BufReader, BufRead};
use std::fs::File;

fn main() {
  let file_path = "../data.txt";
  let mut vectors = Vec::new();
  let mut elf_vec = Vec::new();
  let mut current_elf = 0;

  let file = File::open(file_path).unwrap();
  // Read all of it into the vector (including the newline)
  for line in BufReader::new(file).lines() {
    vectors.push(line.unwrap());
  }
  // let mut current_elf: i32 = 0;
  for i in 0..vectors.len(){
    if !vectors[i].is_empty() {
      current_elf += vectors[i].parse::<i32>().unwrap();
    }
    else{
      elf_vec.push(current_elf);
      current_elf = 0;
    }
  }
  elf_vec.sort();
  


  println!("Part 1 {:?}", elf_vec.last().unwrap());
  println!("Part 2 {:?}", elf_vec.windows(3).last().iter().fold(0, |acc, x| acc + x[0] + x[1] + x[2]));
}