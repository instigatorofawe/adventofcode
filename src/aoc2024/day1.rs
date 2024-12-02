use std::collections::HashMap;
use std::io::BufRead;

fn part_a(lines: &Vec<String>) {
    let values: Vec<Vec<i32>> = lines
        .iter()
        .map(|x| {
            x.split_whitespace()
                .map(|y| y.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let mut left: Vec<i32> = values.iter().map(|x| *x.first().unwrap()).collect();
    let mut right: Vec<i32> = values.iter().map(|x| *x.last().unwrap()).collect();

    left.sort();
    right.sort();

    let result: i32 = left
        .into_iter()
        .zip(right.into_iter())
        .map(|(a, b)| i32::abs(a - b))
        .sum();

    println!("{result}")
}

fn part_b(lines: &Vec<String>) {
    let values: Vec<Vec<i32>> = lines
        .iter()
        .map(|x| {
            x.split_whitespace()
                .map(|y| y.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let left: Vec<i32> = values.iter().map(|x| *x.first().unwrap()).collect();
    let mut right: HashMap<i32, i32> = HashMap::new();

    values.iter().for_each(|x| {
        let key = x.last().unwrap();
        match right.get(key) {
            Some(count) => {
                right.insert(*key, count + 1);
            }
            None => {
                right.insert(*key, 1);
            }
        }
    });

    let result: i32 = left
        .into_iter()
        .map(|x| match right.get(&x) {
            Some(i) => x * i,
            None => 0,
        })
        .sum();

    println!("{result}")
}

pub fn run() {
    let lines: Vec<String> = std::io::stdin()
        .lock()
        .lines()
        .map(|x| x.unwrap())
        .collect();

    part_a(&lines);
    part_b(&lines);
}
