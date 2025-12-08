import unittest
import day1
   


# Das ist der Test-Block
class MeinTest(unittest.TestCase):
    def test_1(self):
        startpos = 1
        expected = 0
        result = day1.get_pos(startpos,-1)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_2(self):
        startpos = 1
        expected = 99
        result = day1.get_pos(startpos,-2)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_3(self):
        startpos = 50
        expected = 50
        result = day1.get_pos(startpos,1000)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_4(self):
        startpos = 35
        expected = 0
        result = day1.get_pos(startpos,65)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    
    
    
    
    def test_5(self):
        startpos = 35
        expected = 1
        result = day1.overflows(startpos,65)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_6(self):
        startpos = 10
        expected = 0
        result = day1.overflows(startpos,-10)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_7(self):
        startpos = 10
        expected = 1
        result = day1.overflows(startpos,-11)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")

    def test_8(self):
        startpos = 10
        expected = 2
        result = day1.overflows(startpos,200)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_9(self):
        startpos = 10
        expected = 2
        result = day1.overflows(startpos,200)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_10(self):
        pos = 50
        for zeile in day1.zeilen_liste:
            pos, overflows = day1.handle_line(zeile,pos)
            self.assertFalse(pos < 0 or pos > 99,"Position außerhalb von 0-99!")
    def test_11(self):
        startpos = 10
        expected = 1
        result = day1.overflows(startpos,90)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_12(self):
        startpos = 10
        expected = 0
        result = day1.overflows(startpos,89)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    
    
    # def test_0(self):
    #     startpos = 3
    #     expected = 3
    #     result = day1.overflows(startpos,-3)
    #     self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    # def test_(self):
    #     startpos = 3
    #     expected = 3
    #     result = day1.overflows(startpos,-3)
    #     self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    # def test_15(self):
    #     startpos = 3
    #     expected = 3
    #     result = day1.overflows(startpos,-3)
    #     self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    # def test_16(self):
    #     startpos = 3
    #     expected = 3
    #     result = day1.overflows(startpos,-3)
    #     self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")


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
            (-1,   1),   # Sofort raus -> -1
            (-99,  1),   # Immer noch im ersten Minus-Block
            (-100, 1),   # Exakt die Grenze (Python Logik: -100/100 = -1)
            (-101, 2),   # JETZT sind wir im zweiten Block (-2)
            (-199, 2),   
            (-200, 2),   # Exakt zwei volle Blöcke
            (-201, 3)    # Dritter Block beginnt
        ]

        for move, expected in test_cases:
            with self.subTest(move=move):
                result = day1.overflows(startpos, move)
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
                result = day1.overflows(startpos, move)
                self.assertEqual(result, expected,
                    f"Fail bei Start={startpos}, Move={move}. Erwartet: {expected}, Ist: {result}")

# Startet die Tests, wenn man die Datei ausführt
if __name__ == '__main__':
    unittest.main()