use std::collections::HashMap;
use std::io::BufRead;

pub fn run() {
    let mut numbers: Vec<Vec<(u32, usize, usize)>> = Vec::new();
    let mut symbols: Vec<Vec<usize>> = Vec::new();
    let mut gears: HashMap<(usize, usize), Vec<u32>> = HashMap::new();

    std::io::stdin()
        .lock()
        .lines()
        .enumerate()
        .for_each(|(row, line)| {
            let line = line.unwrap();

            let mut current_numbers: Vec<(u32, usize, usize)> = Vec::new();
            let mut current_symbols: Vec<usize> = Vec::new();

            let mut current_start: Option<usize> = None;
            let mut current_value: u32 = 0;

            line.chars().enumerate().for_each(|(i, c)| {
                if c.is_numeric() {
                    if current_start.is_none() {
                        current_start = Some(i);
                    }
                    current_value = current_value * 10 + c.to_digit(10).unwrap();
                } else {
                    if let Some(j) = current_start {
                        current_numbers.push((current_value, j, i - 1));
                        current_start = None;
                        current_value = 0;
                    }

                    if c == '*' {
                        current_symbols.push(i);
                        gears.insert((row, i), Vec::new());
                    }
                }
            });

            if let Some(j) = current_start {
                current_numbers.push((current_value, j, line.len() - 1));
            }

            numbers.push(current_numbers);
            symbols.push(current_symbols);
        });

    numbers.into_iter().enumerate().for_each(|(i, number_row)| {
        for (value, start, end) in number_row {
            if i > 0 {
                for j in symbols[i - 1].clone() {
                    if (start as i32 - 1..=end as i32 + 1).contains(&(j as i32)) {
                        gears.get_mut(&(i - 1, j)).unwrap().push(value);
                    }
                }
            }
            if i < symbols.len() - 1 {
                for j in symbols[i + 1].clone() {
                    if (start as i32 - 1..=end as i32 + 1).contains(&(j as i32)) {
                        gears.get_mut(&(i + 1, j)).unwrap().push(value);
                    }
                }
            }
            for j in symbols[i].clone() {
                if (start as i32 - 1..=end as i32 + 1).contains(&(j as i32)) {
                    gears.get_mut(&(i, j)).unwrap().push(value);
                }
            }
        }
    });

    let mut total: u32 = 0;

    gears.values().filter(|x| x.len() == 2).for_each(|x| {
        total += x.iter().product::<u32>();
    });

    println!("{total}");
}
