use std::io::BufRead;

pub fn kmp_preprocess(pattern: &String) -> Vec<i32> {
    let mut result = vec![-1; pattern.len() + 1];
    let mut candidate: i32 = 0;

    for i in 1..pattern.len() {
        if pattern[i..i + 1] == pattern[candidate as usize..candidate as usize + 1] {
            result[i] = result[candidate as usize]
        } else {
            result[i] = candidate;

            while candidate >= 0
                && pattern[i..i + 1] != pattern[candidate as usize..candidate as usize + 1]
            {
                candidate = result[candidate as usize];
            }
        }

        candidate += 1;
    }
    result[pattern.len()] = candidate;

    return result;
}

pub fn kmp_search(text: &String, pattern: &String, table: Option<&Vec<i32>>) -> Vec<usize> {
    let mut result: Vec<usize> = Vec::new();
    let mut j: i32 = 0;
    let mut k: i32 = 0;

    let lookup: &Vec<i32>;
    let lookup_table: Vec<i32>;
    match table {
        Some(x) => {
            lookup = x;
        }
        _ => {
            lookup_table = kmp_preprocess(&pattern);
            lookup = &lookup_table;
        }
    }

    while j < text.len() as i32 {
        if text[j as usize..j as usize + 1] == pattern[k as usize..k as usize + 1] {
            j += 1;
            k += 1;
            if k == pattern.len() as i32 {
                result.push((j - k) as usize);
                k = lookup[k as usize];
            }
        } else {
            k = lookup[k as usize];
            if k < 0 {
                j += 1;
                k = 0;
            }
        }
    }

    return result;
}

pub fn run() {
    let patterns = vec![
        "one".to_string(),
        "two".to_string(),
        "three".to_string(),
        "four".to_string(),
        "five".to_string(),
        "six".to_string(),
        "seven".to_string(),
        "eight".to_string(),
        "nine".to_string(),
    ];
    let values: Vec<u32> = (1..=9).collect();
    let tables: Vec<Vec<i32>> = patterns.iter().map(|x| kmp_preprocess(x)).collect();

    let result: Vec<u32> = std::io::stdin()
        .lock()
        .lines()
        .into_iter()
        .map(|x| {
            let text = x.unwrap();

            let mut y: Vec<(usize, u32)> = patterns
                .iter()
                .zip(values.iter())
                .zip(tables.iter())
                .map(|((pattern, value), table)| {
                    return kmp_search(&text, &pattern, Some(table))
                        .into_iter()
                        .map(|index| (index, *value));
                })
                .flatten()
                .collect();

            let digits: Vec<(usize, u32)> = text
                .chars()
                .into_iter()
                .enumerate()
                .filter(|(i, y)| y.is_numeric())
                .map(|(i, y)| (i, y.to_digit(10).unwrap()))
                .collect();

            y.extend(digits.into_iter());

            y.sort();

            return y[0].1 * 10 + y[y.len() - 1].1;
        })
        .collect();

    let final_sum: u32 = result.into_iter().sum();
    println!("{final_sum}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_kmp_preprocess() {
        assert_eq!(
            kmp_preprocess(&"abacababc".to_string()),
            vec![-1, 0, -1, 1, -1, 0, -1, 3, 2, 0]
        );

        assert_eq!(
            kmp_preprocess(&"abcdabd".to_string()),
            vec![-1, 0, 0, 0, -1, 0, 2, 0]
        );
    }

    #[test]
    fn test_kmp_search() {
        assert_eq!(
            kmp_search(&"asdfasdf".to_string(), &"asdf".to_string(), None),
            vec![0, 4]
        );

        assert_eq!(
            kmp_search(&"zerone".to_string(), &"one".to_string(), None),
            vec![3]
        );
    }
}
