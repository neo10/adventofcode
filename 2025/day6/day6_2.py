def load_data(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return lines


def get_grid(lines: list[str]) -> list[str]:
    width = max(len(line) for line in lines)
    return [line.ljust(width, " ") for line in lines]


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
    for x in range(len(grid)):
        lineList: list[str] = []
        for i in range(0, len(grid[x]), numberLength + 1):
            number = grid[x][i : i + numberLength]
            lineList.append(number)
        result.append(lineList)

    return result


lines = load_data("test.txt")
grid = get_grid(lines)
maxDigits = get_max_digits(grid)
grid_array = get_grid_array(grid, maxDigits)
for line in grid_array:
    print(line)
