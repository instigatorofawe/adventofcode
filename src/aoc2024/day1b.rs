use std::collections::HashMap;
use std::io::BufRead;

pub fn run() {
    let mut counts: HashMap<i32, i32> = HashMap::new();

    let lines: Vec<Vec<i32>> = std::io::stdin()
        .lock()
        .lines()
        .map(|x| {
            x.unwrap()
                .split_whitespace()
                .map(|y| y.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let left: Vec<i32> = lines.iter().map(|x| *x.first().unwrap()).collect();
    lines.iter().for_each(|x| {
        let key = x.last().unwrap();
        match counts.get(key) {
            Some(count) => {
                counts.insert(*key, *count + 1);
            }
            None => {
                counts.insert(*key, 1);
            }
        }
    });

    let result: i32 = left
        .into_iter()
        .map(|x| match counts.get(&x) {
            Some(i) => x * i,
            None => 0,
        })
        .sum();

    println!("{result}")
}
