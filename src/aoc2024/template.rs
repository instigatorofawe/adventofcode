use std::io::BufRead;

fn part_a(lines: &Vec<String>) {}

fn part_b(lines: &Vec<String>) {}

pub fn run() {
    let lines: Vec<String> = std::io::stdin()
        .lock()
        .lines()
        .map(|x| x.unwrap())
        .collect();

    part_a(&lines);
    part_b(&lines);
}
