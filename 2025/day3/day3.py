input_array = []

with open('./input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()            
        zahlen = [int(c) for c in line] 
        input_array.append(zahlen)

print(input_array)
def quick_sort(line:list[int], reverse:bool = False)->list[int]:
    if len(line) == 1 or len(line) == 0:
        return line
    ref_number = line.pop(0)
    print(ref_number)
    smaller_numbers = []
    bigger_numbers = []
    for number in line:
        if number <= ref_number:
            smaller_numbers.append(number)
        else:
            bigger_numbers.append(number)
    
    if reverse == False:
        return quick_sort(smaller_numbers,reverse) + [ref_number] + quick_sort(bigger_numbers,reverse)
    else:
        return quick_sort(bigger_numbers,reverse) + [ref_number] + quick_sort(smaller_numbers,reverse)

def get_index_from_max_number(line: list[int], start_index: int = 0,stop_index:int = len(line)) -> int:
    max = 0
    number = 0
    max_index = 0
    for i in range(start_index,stop_index):
        number = line[i]
        if number > max:
            max = number
            max_index = i
    return max_index


solution1 = 0
for x in input_array:
    print("------------NEW LINE----------")
    print(x)
    #x = quick_sort(x,True)
    #print(x)
    max1_index = get_index_from_max_number(x,stop_index=len(x)-1)
    max2_index = get_index_from_max_number(x,max1_index+1)
    max_num1 = x[max1_index]
    max_num2 = x[max2_index]
    max_volatge = max_num1*10 + max_num2
    print(max_volatge)
    solution1 += max_volatge

print("Lösung1: ",solution1)