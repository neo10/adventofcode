
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
    rawPos = pos + move
    return rawPos % 100
def overflows(pos, move)->int:
    rawPos = pos + move
    if rawPos < 0:
        return 1 + (abs(rawPos) // 100)
    else:
        return rawPos // 100

#Teil1
solution = 0
pos = 50
for zeile in zeilen_liste:
    overflows = 0
    pos, overflows = handle_line(zeile,pos)
    print("New Pos: ",pos)
    if pos == 0:
        solution += 1
    went_over_0 += overflows


print("Lösung Genau 0: ", solution)
print("Lösung Genau 0 + Overflows: ", solution + went_over_0)

print(handle_line("R1000",50))

