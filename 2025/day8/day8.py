from __future__ import annotations

import math
from dataclasses import dataclass, field


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


@dataclass
class JunctionBox:
    id: int
    x_pos: int
    y_pos: int
    z_pos: int


@dataclass
class Wire:
    left_box: JunctionBox
    right_box: JunctionBox
    distance: float


@dataclass
class UnionFind:
    boxes: list[JunctionBox]
    parent: dict[int, int] = field(init=False)
    sizes: dict[int, int] = field(init=False)
    last_connection: tuple[JunctionBox, JunctionBox] | None = field(init=False, default=None)

    def __post_init__(self):
        self.parent = {box.id: box.id for box in self.boxes}
        self.sizes = {box.id: 1 for box in self.boxes}

    def find(self, box: JunctionBox) -> int:
        current = box.id

        while self.parent[current] != current:
            current = self.parent[current]
        return current

    def connect(self, left: JunctionBox, right: JunctionBox) -> None:
        left_root = self.find(left)
        right_root = self.find(right)

        if left_root != right_root:
            self.last_connection = (left, right)
            self.parent[right_root] = left_root
            self.sizes[left_root] += self.sizes[right_root]
            del self.sizes[right_root]

    def get_sizes(self) -> dict[int, int]:
        return self.sizes


def get_wires(boxes: list[JunctionBox]) -> list[Wire]:
    wires = []
    for i in range(len(boxes) - 1):
        boxA = boxes[i]
        for i2 in range(i + 1, len(boxes)):
            boxB = boxes[i2]
            wires.append(Wire(boxA, boxB, calculate_distance(boxA, boxB)))

    return wires


def get_junction_boxes(coordinates: list[str]) -> list[JunctionBox]:
    junction_boxes: list[JunctionBox] = []
    for i, coordinate in enumerate(coordinates):
        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        junction_boxes.append(JunctionBox(i, x, y, z))
    return junction_boxes


coordinates = get_input("data.txt")
junction_boxes = get_junction_boxes(coordinates)
wires = get_wires(junction_boxes)
wires.sort(key=lambda wire: wire.distance)
union = UnionFind(junction_boxes)

# All the logic happens here
for wire in wires[:1000]:
    union.connect(wire.left_box, wire.right_box)


sizes = sorted(union.get_sizes().values(), reverse=True)
solution1 = sizes[0] * sizes[1] * sizes[2]
print(f"Solution1={solution1}")


# Part2:
union2 = UnionFind(junction_boxes)
for wire in wires:
    union2.connect(wire.left_box, wire.right_box)

solution2 = union2.last_connection[0].x_pos * union2.last_connection[1].x_pos
print(f"Solution2={solution2}")
