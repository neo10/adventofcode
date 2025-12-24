with open('./data.txt', 'r', encoding='utf-8') as f:
    input = f.read().strip()

bereiche = []
for teil in input.split(','):
    a, b = teil.split('-')
    bereiche.append([int(a), int(b)])


def is_digits_repeated_twice(number:int)-> bool:
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
    
def is_repeated_any_number(number:int)->bool:
    anzahl_ziffern = len(str(abs(number)))
    zahl_string = str(abs(number))
    if anzahl_ziffern <= 1:
        return False
    intervalle = [i for i in range(1, anzahl_ziffern + 1) 
          if anzahl_ziffern % i == 0 and i != anzahl_ziffern]
    string_to_compare = ""
    is_equal = False
    for intervall in intervalle:
        is_equal = True
        for i in range(0,anzahl_ziffern,intervall):
            if string_to_compare != zahl_string[i:i+intervall] and i > 0:
                is_equal = False
                break
            string_to_compare = zahl_string[i:i+intervall]
        if is_equal == True:
            return True
    return False
    
    

solution1 = 0
solution2 = 0
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
        if is_repeated_any_number(number):
            solution2 += number
print("Lösung1: ",solution1)
print("Lösung2: ",solution2)

print(is_repeated_any_number(123123123))


