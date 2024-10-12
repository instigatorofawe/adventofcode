use std::collections::HashSet;
use std::io::BufRead;

pub fn run() {
    let symbol_lookup: HashSet<char> =
        HashSet::from(['*', '#', '$', '+', '-', '=', '@', '&', '%', '/']);

    let mut numbers: Vec<Vec<(u32, usize, usize)>> = Vec::new();
    let mut symbols: Vec<Vec<usize>> = Vec::new();

    std::io::stdin().lock().lines().for_each(|line| {
        let line = line.unwrap();

        let mut current_numbers: Vec<(u32, usize, usize)> = Vec::new();
        let mut current_symbols: Vec<usize> = Vec::new();

        let mut current_start: Option<usize> = None;
        let mut current_value: u32 = 0;

        line.chars().enumerate().for_each(|(i, c)| {
            if c.is_numeric() {
                match current_start {
                    None => {
                        current_start = Some(i);
                    }
                    _ => {}
                }
                current_value = current_value * 10 + c.to_digit(10).unwrap();
            } else {
                match current_start {
                    Some(j) => {
                        current_numbers.push((current_value, j, i - 1));
                        current_start = None;
                        current_value = 0;
                    }
                    _ => {}
                }

                if symbol_lookup.contains(&c) {
                    current_symbols.push(i);
                }
            }
        });

        match current_start {
            Some(j) => {
                current_numbers.push((current_value, j, line.len() - 1));
            }
            _ => {}
        }

        numbers.push(current_numbers);
        symbols.push(current_symbols);
    });

    let mut total: u32 = 0;

    numbers.into_iter().enumerate().for_each(|(i, number_row)| {
        for (value, start, end) in number_row {
            if i == 0 {
                for j in symbols[i].iter().chain(symbols[i + 1].iter()) {
                    if (start as i32 - 1..=end as i32 + 1).contains(&(*j as i32)) {
                        total += value;
                        break;
                    }
                }
            } else if i == symbols.len() - 1 {
                for j in symbols[i - 1].iter().chain(symbols[i].iter()) {
                    if (start as i32 - 1..=end as i32 + 1).contains(&(*j as i32)) {
                        total += value;
                        break;
                    }
                }
            } else {
                for j in symbols[i - 1]
                    .iter()
                    .chain(symbols[i].iter())
                    .chain(symbols[i + 1].iter())
                {
                    if (start as i32 - 1..=end as i32 + 1).contains(&(*j as i32)) {
                        total += value;
                        break;
                    }
                }
            }
        }
    });

    println!("{total}");
}
