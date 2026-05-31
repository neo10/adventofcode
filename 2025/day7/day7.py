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


def count_timelines(grid: list[list[str]]) -> int:
    start_index = grid[0].index("S")
    positions: dict[int, int] = {start_index: 1}
    counter = 1
    for row in grid:
        next_positions: dict[int, int] = {}
        for position, amount in positions.items():
            if position < 0 or position >= len(row):
                continue
            if row[position] == "^":
                counter += amount
                newPos1 = position - 1
                newPos2 = position + 1
                next_positions[newPos1] = next_positions.get(newPos1, 0) + amount
                next_positions[newPos2] = next_positions.get(newPos2, 0) + amount
            else:
                next_positions[position] = next_positions.get(position, 0) + amount

        positions = next_positions

    return counter


grid = load_data("data.txt")

start_index = grid[0].index("S")

solution = count_splits([start_index], grid, 0)
solution2 = count_timelines(grid)

print(f"Lösung1={solution}")
print(f"Lösung2={solution2}")
