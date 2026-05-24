import math


def load_data(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return lines


def get_grid(lines: list[str]) -> list[str]:
    width = max(len(line) for line in lines)
    return [line.ljust(width, " ") for line in lines]


def calculate_solution(numbers: list[int], calc_symbol: str) -> int:
    match calc_symbol:
        case "+":
            result = sum(numbers)
        case "*":
            result = math.prod(numbers)
        case _:
            raise ValueError(f"Unbekannter Operator: {calc_symbol}")

    return result


def get_grid_array(grid: list[str], indexes: list[int]) -> list[list[str]]:
    result: list[list[str]] = []
    for line in grid:
        line_list: list[str] = []
        for i in range(len(indexes) - 1):
            start = indexes[i] + 1
            end = indexes[i + 1]
            number_string = line[start:end]
            line_list.append(number_string)
        result.append(line_list)

    return result


def get_group_indexes(grid: list[str]) -> list[int]:
    result: list[int] = []
    result.append(-1)
    for x in range(len(grid[0])):
        headerChar = grid[0][x]
        if headerChar == " ":
            border = True
            for y in range(len(grid)):
                if grid[y][x] != " ":
                    border = False
                    break
            if border:
                result.append(x)

    result.append(len(grid[0]))
    return result


def get_calc_symbol(input_string: str) -> str:
    for char in input_string:
        if char == "*":
            return "*"
        elif char == "+":
            return "+"
    raise ValueError(f"Kein Operator gefunden: {input_string}")


def get_solution(grid_array: list[list[str]]) -> int:
    result = 0
    for x in range(len(grid_array[0])):
        numbers: list[int] = []
        for num in range(len(grid_array[0][x])):
            number_chars = ""
            # Ziffern werden spaltenweise zu Zahlen zusammengesetzt.
            for y in range(len(grid_array)):
                char = grid_array[y][x][num]
                if char.isdigit():
                    number_chars += char

            if number_chars:
                numbers.append(int(number_chars))
        calc_symbol = get_calc_symbol(grid_array[-1][x])
        result += calculate_solution(numbers, calc_symbol)

    return result


lines = load_data("data.txt")
grid = get_grid(lines)
indexes = get_group_indexes(grid)
grid_array = get_grid_array(grid, indexes)
solution = get_solution(grid_array)
print(f"Lösung={solution}")
