def load_data(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return lines


def get_grid(lines: list[str]) -> list[str]:
    width = max(len(line) for line in lines)
    return [line.ljust(width, " ") for line in lines]


lines = load_data("test.txt")
print(lines)

grid = get_grid(lines)
print(grid)
for line in grid:
    print(line)
    for elem in line:
        print(elem)

# Build Blocks
