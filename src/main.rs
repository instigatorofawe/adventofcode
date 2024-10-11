mod aoc2023;

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
            _ => println!("Day not found!"),
        },
        _ => println!("Year not found!"),
    }
}
