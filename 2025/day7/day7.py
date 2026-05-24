def load_data(path: str) -> list[list[str]]:
    with open(path, encoding="utf-8") as f:
        result: list[list[str]] = []

        lines = f.read().splitlines()
        result = [list(element) for element in lines]

        return result


def count_splits(positions_now: list[int], grid: list[list[str]], index_row: int) -> int:
    if index_row >= len(grid):
        return 0
    positions: list[int] = []
    counter = 0
    for position in positions_now:
        if position < 0 or position >= len(grid[0]):
            continue
        if grid[index_row][position] == "^":
            positions.append(position - 1)
            positions.append(position + 1)
            counter += 1
        else:
            positions.append(position)

    positions = list(set(positions))
    return counter + count_splits(positions, grid, index_row + 1)


grid = load_data("data.txt")

start_index = grid[0].index("S")

solution = count_splits([start_index], grid, 0)

print(f"Lösung1={solution}")
