input_array = []

with open("./data.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        zeichen = [str(c) for c in line]
        input_array.append(zeichen)


def is_roll_of_paper(array: list[str], index_y: int, index_x: int) -> bool:
    if array[index_y][index_x] == "@":
        return True
    return False


solution1 = 0
neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
max_i = len(input_array) - 1
max_k = len(input_array[0]) - 1
for i in range(len(input_array)):
    for k in range(len(input_array[i])):
        neighborRolls = 0
        is_roll = input_array[i][k] == "@"
        if not (is_roll):
            continue
        for di, dk in neighbor_offsets:
            ni = i + di
            nk = k + dk
            if not (0 <= ni <= max_i and 0 <= nk <= max_k):
                continue
            neighbor = input_array[ni][nk]
            if neighbor == "@":
                neighborRolls += 1

        if neighborRolls < 4:
            solution1 += 1

print("solution1: ", solution1)


# Solution 2
def get_indexes_of_rolls(array: list[str]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] != "@":
                continue
            amount_rolls = 0
            # print("checking neighbours of: ",array[y][x])
            for offset in neighbor_offsets:
                ny = y + offset[0]
                nx = x + offset[1]

                if ny < 0 or ny >= len(array) or nx >= len(array[y]) or nx < 0:
                    continue
                # print(array[ny][nx])
                if array[ny][nx] == "@":
                    amount_rolls += 1

            if amount_rolls < 4:
                result.append((y, x))

    return result


counter = 0

while len(get_indexes_of_rolls(input_array)) > 0:
    indexes = get_indexes_of_rolls(input_array)
    counter += len(indexes)
    for y, x in indexes:
        input_array[y][x] = "."

print("Solution2: ", counter)
