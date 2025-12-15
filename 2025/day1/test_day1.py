import unittest
import day1

class TestOverflows(unittest.TestCase):

    # ---------------------------------------------------------------
    # 1. NEGATIV-TESTS (Start bei 0)
    # Wir stehen ganz links (0). Jeder Schritt nach links löst sofort Overflow aus.
    # ---------------------------------------------------------------
    def test_negative_moves_from_zero(self):
        startpos = 0
        
        # Format: (Bewegung, Erwarteter Overflow)
        test_cases = [
            (0,     0),   # Keine Bewegung
            (-1,   0),   # Sofort raus -> -1
            (-99,  0),   # Immer noch im ersten Minus-Block
            (-100, 1),   # Exakt die Grenze (Python Logik: -100/100 = -1)
            (-101, 1),   # JETZT sind wir im zweiten Block (-2)
            (-199, 1),   
            (-200, 2),   # Exakt zwei volle Blöcke
            (-201, 2)    # Dritter Block beginnt
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected, 
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

    # ---------------------------------------------------------------
    # 2. POSITIV-TESTS (Start bei 0)
    # Wir stehen bei 0. Wir müssen erst 100 schaffen für den ersten Overflow.
    # ---------------------------------------------------------------
    def test_positive_moves_from_zero(self):
        startpos = 0
        
        test_cases = [
            (1,    0),
            (99,   0),    # Wir landen auf 99 -> Alles gut (0 Overflows)
            (100,  1),    # Wir landen auf 100 -> 1x Overflow
            (101,  1),
            (199,  1),
            (200,  2),    # Exakt 2x Overflow
            (299,  2),
            (300,  3)
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.count_zero_crossings_only(startpos, move)
                self.assertEqual(result, expected,
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

# Startet die Tests, wenn man die Datei ausführt
if __name__ == '__main__':
    unittest.main()