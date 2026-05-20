def load_data(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return lines


def get_grid(lines: list[str]) -> list[str]:
    width = max(len(line) for line in lines)
    return [line.ljust(width, " ") for line in lines]


def calculate_solution(numbers: list[int], calcSymbol: str) -> int:
    match calcSymbol:
        case "+":
            result = 0
            for number in numbers:
                result += number
        case "*":
            result = 1
            for number in numbers:
                result *= number
        case _:
            raise ValueError(f"Unbekannter Operator: {calcSymbol}")

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


def getCalcSymbol(inputString: str) -> str:
    for char in inputString:
        if char == "*":
            return "*"
        elif char == "+":
            return "+"


def get_solution(grid_array: list[list[str]]) -> int:
    result = 0
    for x in range(len(grid_array[0])):
        numbers: list[int] = []
        for num in range(len(grid_array[0][x])):
            number_chars = ""
            for y in range(len(grid_array)):
                char = grid_array[y][x][num]
                if char.isdigit():
                    number_chars += char

            if number_chars:
                numbers.append(int(number_chars))
        calcSymbol = getCalcSymbol(grid_array[-1][x])
        result += calculate_solution(numbers, calcSymbol)

    return result


lines = load_data("data.txt")
grid = get_grid(lines)
indexes = get_group_indexes(grid)
grid_array = get_grid_array(grid, indexes)
solution = get_solution(grid_array)
print(f"Lösung={solution}")
