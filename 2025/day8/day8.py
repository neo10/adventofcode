import math
from dataclasses import dataclass


def get_input(file_path: str) -> list[str]:
    with open(file_path, encoding="utf-8") as f:
        result: list[str] = []

        result = f.read().splitlines()

        result = [[int(number) for number in line.split(",")] for line in result]
        return result


def calculate_distance(box_a: JunctionBox, box_b: JunctionBox) -> float:
    dx = box_a.x_pos - box_b.x_pos
    dy = box_a.y_pos - box_b.y_pos
    dz = box_a.z_pos - box_b.z_pos

    return math.sqrt(dx**2 + dy**2 + dz**2)


@dataclass(frozen=True)
class JunctionBox:
    id: int
    x_pos: int
    y_pos: int
    z_pos: int


coordinates = get_input("test.txt")
junction_boxes: list[JunctionBox] = []
for i, coordinate in enumerate(coordinates):
    x = coordinate[0]
    y = coordinate[1]
    z = coordinate[2]
    junction_boxes.append(JunctionBox(i, x, y, z))

print(junction_boxes)
for box in junction_boxes:
    print(calculate_distance(junction_boxes[0], box))
