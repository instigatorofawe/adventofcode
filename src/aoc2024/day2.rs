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
    let differences: Vec<Vec<i32>> = values
        .into_iter()
        .map(|x| {
            let len = x.len();
            x.as_slice()[..len - 1]
                .iter()
                .zip(x.as_slice()[1..len].iter())
                .map(|(a, b)| b - a)
                .collect()
        })
        .collect();

    let result: i32 = differences
        .into_iter()
        .map(|x| {
            ((x.iter().all(|y| *y < 0) || x.iter().all(|y| *y > 0))
                && x.iter().all(|y| i32::abs(*y) <= 3)) as i32
        })
        .sum();

    println!("{result}");
}

fn part_b(lines: &Vec<String>) {
    let result: i32 = lines
        .iter()
        .map(|x| {
            x.split_whitespace()
                .map(|y| y.parse::<i32>().unwrap())
                .collect()
        })
        .map(|values: Vec<i32>| match evaluate(&values, None) {
            true => 1,
            false => {
                for i in 0..values.len() {
                    if evaluate(&values, Some(i)) {
                        return 1;
                    }
                }
                return 0;
            }
        })
        .sum();
    println!("{result}");
}

fn evaluate(values: &Vec<i32>, i: Option<usize>) -> bool {
    match i {
        None => {
            let len = values.len();
            let differences: Vec<i32> = values.as_slice()[..len - 1]
                .iter()
                .zip(values.as_slice()[1..len].iter())
                .map(|(a, b)| *a - *b)
                .collect();
            (differences.iter().all(|y| *y < 0) || differences.iter().all(|y| *y > 0))
                && differences.iter().all(|y| i32::abs(*y) <= 3)
        }
        Some(j) => {
            let values: Vec<i32> = values
                .into_iter()
                .enumerate()
                .filter(|(i, _)| *i != j)
                .map(|(_, x)| *x)
                .collect();
            let len = values.len();
            let differences: Vec<i32> = values.as_slice()[..len - 1]
                .iter()
                .zip(values.as_slice()[1..len].iter())
                .map(|(a, b)| *a - *b)
                .collect();
            (differences.iter().all(|y| *y < 0) || differences.iter().all(|y| *y > 0))
                && differences.iter().all(|y| i32::abs(*y) <= 3)
        }
    }
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
