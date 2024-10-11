use std::io::BufRead;

pub fn run() {
    let result: Vec<u32> = std::io::stdin()
        .lock()
        .lines()
        .into_iter()
        .map(|x| {
            let digits: Vec<u32> = x
                .unwrap()
                .chars()
                .into_iter()
                .filter(|y| y.is_numeric())
                .map(|y| y.to_digit(10).unwrap())
                .collect();
            return digits[0] * 10 + digits[digits.len() - 1];
        })
        .collect();

    let final_sum: u32 = result.into_iter().sum();
    println!("{final_sum}");
}
