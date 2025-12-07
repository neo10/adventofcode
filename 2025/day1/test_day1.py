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
        for zeile in day1.zeilen_liste:
            pos, overflows = day1.handle_line(zeile)
            self.assertFalse(pos < 0 or pos > 99,"Position außerhalb von 0-99!")
   

# Startet die Tests, wenn man die Datei ausführt
if __name__ == '__main__':
    unittest.main()