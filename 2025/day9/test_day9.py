import unittest

import day9


class TestGetSurface(unittest.TestCase):
    def setUp(self):
        self.service = day9.CornerService()

    def test_normal_rectangle(self):
        a = day9.Corner(corner_id=0, x_pos=0, y_pos=0)
        b = day9.Corner(corner_id=1, x_pos=3, y_pos=4)
        self.assertEqual(self.service.get_surface(a, b), 20)

    def test_max_rectangle(self):
        a = day9.Corner(corner_id=0, x_pos=2, y_pos=5)
        b = day9.Corner(corner_id=1, x_pos=11, y_pos=1)
        self.assertEqual(self.service.get_surface(a, b), 50)

    def test_same_x_position_counts_single_column(self):
        a = day9.Corner(corner_id=0, x_pos=5, y_pos=5)
        b = day9.Corner(corner_id=1, x_pos=5, y_pos=9)
        self.assertEqual(self.service.get_surface(a, b), 5)

    def test_same_y_position_counts_single_row(self):
        a = day9.Corner(corner_id=0, x_pos=5, y_pos=5)
        b = day9.Corner(corner_id=1, x_pos=9, y_pos=5)
        self.assertEqual(self.service.get_surface(a, b), 5)

    def test_same_point_gives_minimum_surface(self):
        a = day9.Corner(corner_id=0, x_pos=5, y_pos=5)
        b = day9.Corner(corner_id=1, x_pos=5, y_pos=5)
        self.assertEqual(self.service.get_surface(a, b), 1)

    def test_order_of_corners_does_not_matter(self):
        a = day9.Corner(corner_id=0, x_pos=0, y_pos=0)
        b = day9.Corner(corner_id=1, x_pos=3, y_pos=4)
        self.assertEqual(
            self.service.get_surface(a, b),
            self.service.get_surface(b, a),
        )


if __name__ == "__main__":
    unittest.main()
