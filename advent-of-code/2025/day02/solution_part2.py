from utils.helpers import read_input

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day02/input.txt"
iterator = read_input(path)

def isInvalid(number, length):
    if length == 1:
        return False
    
    for k in range(2, length + 1):
        chunk_size = length // k
        s = str(number)
        chunks = [s[i:i+chunk_size] for i in range(0, length, chunk_size)]
        if all(ch == chunks[0] for ch in chunks):
            return True
    return False
    

result = 0
for line in iterator:
    operation = str(line.strip())
    for item in operation.split(","):
        start = int(item.split("-")[0])
        end = int(item.split("-")[1])
        for number in range(start, end+1):
            length = len(str(number))
            if isInvalid(number, length):
                result += number

print(result)