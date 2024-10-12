use std::collections::HashSet;
use std::io::BufRead;

pub fn run() {
    let mut result: u32 = 0;
    std::io::stdin().lock().lines().for_each(|line| {
        let line = line.unwrap();
        let split_line: Vec<&str> = line.split("|").collect();

        let mut memo: HashSet<&str> = HashSet::new();
        split_line[0]
            .split(":")
            .last()
            .unwrap()
            .split_whitespace()
            .for_each(|x| {
                memo.insert(x);
            });

        let matches: u32 = split_line[1]
            .split_whitespace()
            .map(|x| match memo.contains(x) {
                true => 1,
                false => 0,
            })
            .sum();

        if matches > 0 {
            result += 1 << (matches - 1);
        }
    });

    println!("{result}");
}
