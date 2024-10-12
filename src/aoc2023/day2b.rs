use std::collections::HashMap;
use std::io::BufRead;

pub fn run() {
    let result: u32 = std::io::stdin()
        .lock()
        .lines()
        .map(|x| {
            let x = x.unwrap();
            let binding: Vec<&str> = x.split(":").collect();

            let draws = binding[1].split(";").flat_map(|color_draws| {
                color_draws.split(",").map(|draw| {
                    let split_draws: Vec<&str> = draw.split_whitespace().collect();
                    let color = split_draws[1];
                    let value: u32 = split_draws[0].parse::<u32>().unwrap();
                    (color, value)
                })
            });

            let mut minimum: HashMap<&str, u32> =
                HashMap::from([("red", 0), ("green", 0), ("blue", 0)]);

            draws.for_each(|(color, value)| {
                minimum.insert(color, *minimum.get(color).unwrap().max(&value));
            });

            return minimum.values().product::<u32>();
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
