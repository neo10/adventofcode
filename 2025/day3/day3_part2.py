input_array = []

with open('./input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()            
        zahlen = [int(c) for c in line] 
        input_array.append(zahlen)

def get_max_batteries(digitArray: list[int],start_index:int, digitCount:int) -> str:
    if digitCount > len(digitArray):
       raise ValueError(
            f"digitCount or start_index are not valid for given array"
        )
    if digitCount == 0:
        return ""
    max_digit = 0
    max_index = 0
    end_index = len(digitArray) - digitCount
    for i in range(start_index,end_index + 1):
        digit = digitArray[i]
        if digit > max_digit:
            max_digit = digit
            max_index = i
    #print(max_digit)
    return str(max_digit) + get_max_batteries(digitArray,max_index + 1,digitCount - 1)
    


solution2 = 0
for line in input_array:
    solution2 += int(get_max_batteries(line,0,12))

print(solution2)