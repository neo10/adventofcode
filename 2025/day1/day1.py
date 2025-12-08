
with open('2025/day1/day1.txt', 'r', encoding='utf-8') as f:
    zeilen_liste = f.readlines()

def handle_line(line:str, startpos:int)-> tuple[int,int]:
    match line[0]:
        case "L":
            move = - int(line[1:])
            return get_pos(startpos,move), overflows(startpos,move)
        case "R":
            move = int(line[1:])
            return get_pos(startpos,move), overflows(startpos,move)

        case _:
            print("ERROR: Erster Buchstabe weder R noch L")



def get_pos(pos,move) -> int:
    rawPos = int(pos) + int(move)
    return rawPos % 100
def overflows(pos, move)->int:
    starts_from_0 = 0
    lands_on_zero = 0
    goes_left = 0
    diff = pos + move
    
    if pos == 0 and diff <0:
        starts_from_0 = 1
    if get_pos(pos,move) == 0:
        lands_on_zero = 1
    if diff < 0:
        goes_left = 1
    
    return (diff // 100) - starts_from_0 - lands_on_zero + goes_left

#Teil1
solution = 0
pos = 50
went_over_0 = 0
for zeile in zeilen_liste:
    number_of_overflows = 0
    pos, number_of_overflows = handle_line(zeile,pos)
    print("New Pos: ",pos)
    if pos == 0:
        solution += 1
    went_over_0 += number_of_overflows


print("Lösung Genau 0: ", solution)
print("Lösung Genau 0 + Overflows: ", solution + went_over_0)

print(handle_line("R1000",50))

