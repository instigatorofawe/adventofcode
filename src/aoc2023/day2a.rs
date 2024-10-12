use std::collections::HashMap;
use std::io::BufRead;

pub fn run() {
    let limits: HashMap<&str, u32> = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let result: u32 = std::io::stdin()
        .lock()
        .lines()
        .map(|x| {
            let x = x.unwrap();
            let binding: Vec<&str> = x.split(":").collect();
            let game_id = binding[0]
                .split(" ")
                .last()
                .unwrap()
                .parse::<u32>()
                .unwrap();

            let draws = binding[1].split(";").flat_map(|color_draws| {
                color_draws.split(",").map(|draw| {
                    let split_draws: Vec<&str> = draw.trim().split(" ").collect();
                    let color = split_draws[1];
                    let value: u32 = split_draws[0].parse::<u32>().unwrap();

                    (color, value)
                })
            });

            for (color, value) in draws {
                if limits[color] < value {
                    return 0;
                }
            }

            game_id
        })
        .sum();
    println!("{result}");
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_split() {
        let x: Vec<&str> = "a, b".split(",").map(|z| z.trim()).collect();
        assert_eq!(x, vec!["a", "b"]);
    }
}
