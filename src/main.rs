mod aoc2023;
mod aoc2024;

use clap::Parser;

#[derive(Parser, Debug)]
#[command()]
struct Args {
    /// Which year's solution to run
    #[arg()]
    year: String,

    /// Which day and part's solution to run (e.g. 1a, 1b)
    #[arg()]
    day: String,
}

fn main() {
    let args = Args::parse();

    match args.year.as_str() {
        "2023" => match args.day.as_str() {
            "1a" => aoc2023::day1a::run(),
            "1b" => aoc2023::day1b::run(),
            "2a" => aoc2023::day2a::run(),
            "2b" => aoc2023::day2b::run(),
            "3a" => aoc2023::day3a::run(),
            "3b" => aoc2023::day3b::run(),
            "4a" => aoc2023::day4a::run(),
            "4b" => aoc2023::day4b::run(),
            _ => println!("Day not found!"),
        },
        "2024" => match args.day.as_str() {
            "1a" => aoc2024::day1a::run(),
            "1b" => aoc2024::day1b::run(),
            _ => println!("Day not found!"),
        },
        _ => println!("Year not found!"),
    }
}
