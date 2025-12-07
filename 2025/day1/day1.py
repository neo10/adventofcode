went_over_0 = 0

with open('day1.txt', 'r', encoding='utf-8') as f:
    zeilen_liste = f.readlines()

print(zeilen_liste[0])

# 1. Nur 'def', kein 'function'
# 2. Doppelpunkt am Ende
def handle_zeile(zeile: str, position: int):
    # 3. Zuerst 'match' auf die Variable anwenden
    match zeile[0]:
        case "L":
            newPosition = position - int(getNumber(zeile))
            return get_valid_position(newPosition)

        case "R":
            newPosition = position + int(getNumber(zeile))
            return get_valid_position(newPosition)

        case _:
            print("ERROR: Erster Buchstabe weder R noch L")




def getNumber(zeile):
    return zeile[1:]

# for zeile in zeilen_liste:
#     print(getNumber(zeile))

def get_valid_position(position:int) -> int:
    # print("Aufgerufen mit Position= ", position)
    if position <=99 and position >=0:
        return position
    global went_over_0
    went_over_0 +=1
    if position < 0:
        return get_valid_position(position + 100)
    elif position > 99:
        return get_valid_position(position - 100)

#Teil1
solution = 0
pos = 50
for zeile in zeilen_liste:
    pos = handle_zeile(zeile, pos)
    if pos == 0:
        solution += 1

print(get_valid_position(-1))

print("Lösung: ", solution)
print("Lösung: ", solution + went_over_0)

# test_zeile = "L1000"

# print(handle_zeile(test_zeile,50))
# print(went_over_0)
