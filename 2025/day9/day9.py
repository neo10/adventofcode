from dataclasses import dataclass


def get_input(file_path: str) -> list[tuple[int, int]]:
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

        result: list[tuple[int, int]] = []
        for line in lines:
            x_str, y_str = line.split(",")
            result.append((int(x_str), int(y_str)))
        return result


@dataclass
class Corner:
    corner_id: int
    x_pos: int
    y_pos: int


class CornerService:
    def get_surface(self, a_corner: Corner, b_corner: Corner) -> int:
        diff_x = abs(a_corner.x_pos - b_corner.x_pos) + 1
        diff_y = abs(a_corner.y_pos - b_corner.y_pos) + 1
        return diff_x * diff_y

    def get_maximum_surface(self, corners: list[Corner]) -> list[tuple[Corner, Corner, int]]:
        result: list[tuple[Corner, Corner, int]] = []
        for i in range(len(corners) - 1):
            corner1 = corners[i]
            for i2 in range(i + 1, len(corners)):
                corner2 = corners[i2]
                area = self.get_surface(corner1, corner2)

                result.append((corner1, corner2, area))
        result.sort(key=lambda entry: entry[2], reverse=True)
        return result


def main() -> None:
    corners = get_input("data.txt")
    corner_list = [Corner(i, x, y) for i, (x, y) in enumerate(corners)]

    corner_service = CornerService()
    _, _, solution1 = corner_service.get_maximum_surface(corner_list)[0]
    print(solution1)


if __name__ == "__main__":
    main()
