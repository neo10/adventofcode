input_array = []

with open('./data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()            
        zeichen = [str(c) for c in line] 
        input_array.append(zeichen)


def is_roll_of_paper(array:list[str],index_y:int,index_x:int)->bool:
    if array[index_y][index_x] == '@':
        return True
    
    return False
solution1 = 0
neighbor_offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
max_i = len(input_array) - 1
max_k = len(input_array[0]) - 1
for i in range(len(input_array)):
    for k in range(len(input_array[i])):
        neighborRolls = 0
        is_roll = (input_array[i][k] == '@')
        if not(is_roll):
            continue
        for di, dk in neighbor_offsets:
            ni = i + di
            nk = k + dk
            if not(0 <= ni <= max_i and 0 <= nk <= max_k): continue
            neighbor = input_array[ni][nk]
            if neighbor == '@':
                neighborRolls += 1
        
        if neighborRolls < 4:
            solution1 +=1

print("solution1: ",solution1)







        

        
    