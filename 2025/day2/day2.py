with open('./data.txt', 'r', encoding='utf-8') as f:
    input = f.read().strip()

bereiche = []
for teil in input.split(','):
    a, b = teil.split('-')
    bereiche.append([int(a), int(b)])


def is_digits_repeated_twice(number)-> bool:
    anzahl_ziffern = len(str(abs(number)))
    if anzahl_ziffern % 2 != 0:
        return False

    s = str(abs(number))
    halb = anzahl_ziffern // 2

    first_half = s[:halb]
    second_half = s[halb:]

    if first_half == second_half:
        return True
    else:
        return False

solution1 = 0 
for bereich in bereiche:
    try:
        num1 = bereich[0]
        num2 = bereich[1]
    except ValueError:
        continue
    numbers = range(num1,num2+1)
    for number in numbers:
        if is_digits_repeated_twice(number):
            solution1 += number
    
print("Lösung1: ",solution1)


