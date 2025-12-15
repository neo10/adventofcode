import unittest
import day1

class TestOverflows(unittest.TestCase):

    def test_negative_moves_from_zero(self):
        startpos = 0
        
        test_cases = [
            (0,     0),   
            (-1,   0),   
            (-99,  0),   
            (-100, 1),   
            (-101, 1),   
            (-199, 1),   
            (-200, 2),   
            (-201, 2)    
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected, 
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

    def test_positive_moves_from_zero(self):
        startpos = 0
        
        test_cases = [
            (1,    0),
            (99,   0),   
            (100,  1),    
            (101,  1),
            (199,  1),
            (200,  2),   
            (299,  2),
            (300,  3)
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected,
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

    def test_positive_moves_from_20(self):
        startpos = 20
        
        test_cases = [
            (0,    0),
            (1,    0),   
            (79,  0),    
            (80,  1),
            (81,  1),
            (100,  1),   
            (200,  2),
            (180,  2),
            (181,  2)
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected,
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")
    def test_negative_moves_from_20(self):
        startpos = 20
        
        test_cases = [
            (0,    0),
            (-1,    0),   
            (-19,  0),    
            (-20,  1),
            (-21,  1),
            (-100,  1),   
            (-200,  2),
            (-120,  2),
            (-121,  2)
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected,
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

# Startet die Tests, wenn man die Datei ausführt
if __name__ == '__main__':
    unittest.main()