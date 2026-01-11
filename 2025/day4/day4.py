input_array = []

with open('./test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()            
        zeichen = [str(c) for c in line] 
        input_array.append(zeichen)


def is_roll_of_paper(array:list[str],index_y:int,index_x:int)->bool:
    if array[index_y][index_x] == '@':
        return True
    
    return False

indexes = []
max_index = len(input_array)-1
for i in range(len(input_array)):
    top_index = i-1 if i > 0 else 0
    bottom_index = i+1 if i < max_index else i

    for k in range(len(input_array[i])):
        max_index2 = len(input_array[i])-1
        left_index = k-1 if k > 0 else 0
        right_index = k+1 if k < max_index2 else k

neighbor_indexes = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


        

        
    