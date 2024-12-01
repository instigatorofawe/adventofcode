use std::io::BufRead;

pub fn run() {
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
    let mut left: Vec<i32> = lines.iter().map(|x| *x.first().unwrap()).collect();
    let mut right: Vec<i32> = lines.iter().map(|x| *x.last().unwrap()).collect();

    left.sort();
    right.sort();

    let result: i32 = left
        .into_iter()
        .zip(right.into_iter())
        .map(|(a, b)| i32::abs(a - b))
        .sum();

    println!("{result}")
}
