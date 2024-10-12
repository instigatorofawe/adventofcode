use std::collections::HashMap;
use std::collections::HashSet;
use std::io::BufRead;

pub fn run() {
    let matches: Vec<u32> = std::io::stdin()
        .lock()
        .lines()
        .map(|line| {
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

            return matches;
        })
        .collect();

    let mut memo: HashMap<usize, u32> = HashMap::new();
    fn dp(index: usize, memo: &mut HashMap<usize, u32>, matches: &Vec<u32>) -> u32 {
        if memo.contains_key(&index) {
            return *memo.get(&index).unwrap();
        } else {
            let mut result: u32 = 1;
            for i in 1..=matches[index] {
                result += dp(index + i as usize, memo, matches);
            }
            memo.insert(index, result);

            return result;
        }
    }

    let mut result: u32 = 0;

    for i in 0..matches.len() {
        result += dp(i, &mut memo, &matches);
    }

    println!("{result}");
}
