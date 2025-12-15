
with open('2025/day1/day1.txt', 'r', encoding='utf-8') as f:
    zeilen_liste = f.readlines()



def get_pos(pos,move) -> int:
    rawPos = int(pos) + int(move)
    return rawPos % 100
def count_zero_crossings_only(pos, move)->int:
    endpos = pos + move
    if move == 0 or 0 < endpos <= 99:
        return 0
    if endpos == 0:
        return 1

    if endpos > 99:
        return endpos // 100
    if endpos < 0:
        return (abs(endpos)) // 100 + 0 if pos == 0 else 1

#Teil1
solution1 = 0
solution2 = 0
pos = 50


#Teil1:
for line in zeilen_liste:
    line = line.strip()
    move = int(line[1:]) if line[0] == "R" else -int(line[1:])


    #Teil1:
    if pos == 0:
        solution1 += 1

    #Teil2:
    solution2 += count_zero_crossings_only(pos, move)
    
    
    
    pos = (pos + move) % 100


print("Lösung Genau 0: ", solution1)
print("Lösung Klick auf 0: ", solution2)

