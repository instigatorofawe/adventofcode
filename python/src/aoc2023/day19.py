import sys


def eval_ruleset(values, ruleset):
    for rule in ruleset:
        if ":" in rule:
            destination = rule[rule.index(":") + 1 :]
            rule = rule[: rule.index(":")]
            if ">" in rule:
                var, value = rule.split(">")
                if values[var] > int(value):
                    return destination
            else:
                var, value = rule.split("<")
                if values[var] < int(value):
                    return destination
        else:
            return rule


def part_a(lines: list[str]):
    mode = "rule"
    rulesets = {}
    result = 0

    for line in lines:
        if len(line) == 0:
            mode = "parts"
            continue

        if mode == "rule":
            name = line[: line.index("{")]
            s = line[line.index("{") + 1 : -1]
            rules = s.split(",")
            rulesets[name] = rules

        elif mode == "parts":
            values = {}
            s = line[1:-1].split(",")
            rating = 0
            for x in s:
                name, value = x.split("=")
                value = int(value)
                values[name] = value
                rating += value

            rule = "in"
            while rule not in ["A", "R"]:
                rule = eval_ruleset(values, rulesets[rule])
            if rule == "A":
                result += rating

    print(result)


def eval_range(ranges, rulesets, rule, index) -> int:
    for k in ranges:
        lower, upper = ranges[k]
        if lower > upper:
            return 0

    match rule:
        case "R":
            return 0
        case "A":
            result = 1
            for k in ranges:
                lower, upper = ranges[k]
                result *= upper - lower + 1
            return result

    current_rule = rulesets[rule][index]

    if ":" in current_rule:
        destination = current_rule[current_rule.index(":") + 1 :]
        current_rule = current_rule[: current_rule.index(":")]

        if ">" in current_rule:
            var, value = current_rule.split(">")
            value = int(value)

            # Range that meets criterion
            a = ranges.copy()
            a[var] = (value + 1, a[var][1])

            # Range that doesn't meet criterion
            b = ranges.copy()
            b[var] = (b[var][0], value)

            return eval_range(a, rulesets, destination, 0) + eval_range(
                b, rulesets, rule, index + 1
            )

        else:
            var, value = current_rule.split("<")
            value = int(value)

            # Range that meets criterion
            a = ranges.copy()
            a[var] = (a[var][0], value - 1)

            # Range that doesn't meet criterion
            b = ranges.copy()
            b[var] = (value, b[var][1])

            return eval_range(a, rulesets, destination, 0) + eval_range(
                b, rulesets, rule, index + 1
            )
    else:
        return eval_range(ranges, rulesets, current_rule, 0)


def range_size(ranges):
    result = 1
    for k in ranges:
        result = result * (ranges[k][1] - ranges[k][0] + 1)
    return result


def part_b(lines: list[str]):
    rulesets = {}

    for line in lines:
        if len(line) == 0:
            break

        name = line[: line.index("{")]
        s = line[line.index("{") + 1 : -1]
        rules = s.split(",")
        rulesets[name] = rules

    print(
        eval_range(
            {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)},
            rulesets,
            "in",
            0,
        )
    )


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
