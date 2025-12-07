import unittest
import day1

def handle_line(line:str, startpos:int)-> tuple[int,int]:
    match line[0]:
        case "L":
            newPosition = startpos - int(line[1:])
            return get_real_pos(newPosition),

        case "R":
            newPosition = startpos + int(line[1:])
            return get_real_pos(newPosition)

        case _:
            print("ERROR: Erster Buchstabe weder R noch L")



def get_real_pos(pos):
    if pos < 0:
        return 100 -(-pos % 100)
    elif pos > 99:
        return (pos % 100)
    else:
        return pos
def get_div_amount(pos):
    if pos >= 0 or pos <= 99:
        return pos
    else:
        return (abs(pos) // 100)  


# Das ist der Test-Block
class MeinTest(unittest.TestCase):
    def test_1(self):
        line = "L30"
        startpos = 20
        expected = 90,
        result = handle_line(line,startpos)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_2(self):
        line = "R30"
        startpos = 20
        expected = 50,
        result = handle_line(line,startpos)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_3(self):
        line = "R30"
        startpos = 80
        expected = 10,
        result = handle_line(line,startpos)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_4(self):
        line = "L200"
        startpos = 0
        expected = 0
        result = handle_line(line,startpos)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")

    def test_5(self):
        line = "L200"
        startpos = 1
        expected = 1
        result = handle_line(line,startpos)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_6(self):
        expected = 2
        result = get_div_amount(200)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_7(self):
        expected = 1
        result = get_div_amount(150)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")
    def test_8(self):
        expected = 2
        result = get_div_amount(-250)
        self.assertEqual(result, expected, f"Fehler! Erwartet: {expected}, aber erhalten: {result}")

# Startet die Tests, wenn man die Datei ausführt
if __name__ == '__main__':
    unittest.main()