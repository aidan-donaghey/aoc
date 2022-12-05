use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let pairs  = load_pairs();
    println!("Part 1 Valid: {}", find_num_fully_encapsulated(pairs));
    let pairs2  = load_pairs();
    println!("Part 2 Valid: {}", find_num_any_overlap(pairs2));
}


fn find_num_any_overlap(pairs: Vec<(Vec<u16>, Vec<u16>)>) -> u16 {
    let mut valid: u16 = 0;
    for pair in pairs {
        // First end overlaps with second start
        // Second end overlaps with first start
        if pair.0[0] <= pair.1[0] && pair.0[1] >= pair.1[0] 
        || pair.1[0] <= pair.0[0] && pair.1[1] >= pair.0[0] {
            valid += 1;
        } 
    }
    valid
}

fn find_num_fully_encapsulated(pairs: Vec<(Vec<u16>, Vec<u16>)>) -> u16 {
    let mut valid = 0;
    for pair in pairs {
        if pair.0[0] <= pair.1[0] && pair.0[1] >= pair.1[1] ||
           (pair.1[0] <= pair.0[0] && pair.1[1] >= pair.0[1]) {
            valid += 1;
        }
    }
    valid
}

fn load_pairs() -> Vec<(Vec<u16>, Vec<u16>)> {
    // Loads the Pairs from the file and returns them as a vector.
    let mut pairs = Vec::new();

    let file_path  = "../data.prod";
    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line.unwrap();
        // Feel like I can do the following 3 lines as a map
        let parts = line.split(",").collect::<Vec<&str>>();
        let pair_1: Vec<u16>= parts[0].split("-").map(|x| x.parse::<u16>().unwrap()).collect();
        let pair_2: Vec<u16> = parts[1].split("-").map(|x| x.parse::<u16>().unwrap()).collect();
        pairs.push((pair_1, pair_2));
    }
    pairs
} 