import re
from dataclasses import dataclass, field


def load_data(path: str):
    with open(path, encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    number_rows = []
    for line in lines[:-1]:
        nums = [int(x) for x in re.findall(r"\d+", line)]
        number_rows.append(nums)

    ops = re.findall(r"\S", lines[-1])
    return number_rows, ops


@dataclass
class Calculator:
    def calculate(self, calculation: Calculation) -> int:
        match calculation.calcSymbol:
            case "+":
                return sum(calculation.calcNumbers)
            case "*":
                result = 1
                for n in calculation.calcNumbers:
                    result *= n
                return result
            case _:
                raise ValueError(f"Unknown symbol: {calculation.calcSymbol}")


@dataclass
class Calculation:
    calcSymbol: str
    calcNumbers: list[str] = field(default_factory=list)


def get_calculations(numbers: list[int], operators: list[str]) -> list[Calculation]:
    result: list[Calculation] = []
    for x in range(len(numbers[0])):
        calculation = Calculation(operators[x])
        for y in range(len(numbers)):
            calculation.calcNumbers.append(numbers[y][x])
        result.append(calculation)

    return result


numbers, operators = load_data("test.txt")
print(numbers)
calculations = get_calculations(numbers, operators)

solution1 = 0
calculator = Calculator()
for calculation in calculations:
    solution1 += calculator.calculate(calculation)


print("Solution1: ", solution1)
