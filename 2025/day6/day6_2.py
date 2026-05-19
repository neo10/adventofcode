def load_data(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return lines


def get_grid(lines: list[str]) -> list[str]:
    width = max(len(line) for line in lines)
    return [line.ljust(width, " ") for line in lines]


def calculate_solution(numbers: list[int], calcSymbol: str) -> int:
    print(calcSymbol)
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


def get_max_digits(grid: list[str]) -> int:
    result = 0
    counter = 0
    for line in grid:
        for elem in line:
            if elem.isdigit():
                counter += 1
                if counter > result:
                    result = counter
            else:
                counter = 0
    return result


def get_grid_array(grid: list[str], numberLength: int) -> list[list[str]]:
    result: list[list[str]] = []
    print(grid)
    for x in range(len(grid[0])):
        headerChar = grid[0][x]
        print(f"checking for value={headerChar}")
        if headerChar == " ":
            border = True
            for y in range(len(grid)):
                print(f"x={x}, y={y}, value={grid[y][x]}")
                if grid[y][x] != " ":
                    border = False
                    break
            if border:
                print("BORDER")
        lineList: list[str] = []

    return result


def getCalcSymbol(inputString: str) -> str:
    for char in inputString:
        if char == "*":
            return "*"
        elif char == "+":
            return "+"


def get_solution(grid_array: list[list[str]], maxDigits: int) -> int:
    result = 0
    for x in range(len(grid_array[0])):
        numbers: list[int] = []
        for num in range(maxDigits):
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


lines = load_data("test.txt")
grid = get_grid(lines)
maxDigits = get_max_digits(grid)
grid_array = get_grid_array(grid, maxDigits)
