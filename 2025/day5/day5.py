from bisect import bisect_right


def read_pairs(path: str):
    pairs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            a_str, b_str = line.split("-")
            pairs.append((int(a_str), int(b_str)))
    return pairs


def read_input_numbers(path: str) -> list[int]:
    numbers = []
    second_part = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                second_part = True
                continue

            if second_part:
                numbers.append(int(line))
    return numbers


def merge_input_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    ranges = sorted(ranges, key=lambda x: x[0])

    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def is_number_in_range(number: int, ranges: list[tuple[int, int]]) -> bool:
    starts = [s for s, _ in ranges]
    i = bisect_right(starts, number) - 1

    if i < 0:
        return False

    return number <= ranges[i][1]


validRanges: list[tuple[int, int]] = []

path = "data.txt"

validRanges = read_pairs(path)
merged_ranges = merge_input_ranges(validRanges)
input_numbers = read_input_numbers(path)

solution1 = 0
solution2 = 0

for number in input_numbers:
    if is_number_in_range(number, merged_ranges):
        solution1 += 1


for range in merged_ranges:
    solution2 += (range[1] - range[0]) + 1


print("Solution1: ", solution1)
print("Solution2: ", solution2)
