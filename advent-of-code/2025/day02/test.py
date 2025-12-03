from utils.helpers import read_input
import math

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day02/test.txt"
iterator = read_input(path)

def isInvalid(number):
    length = len(str(number))
    if length % 2 != 0:
        return False
    else:
        x = 10**(length/2)
        quotient = number//x
        remainder = number%x
        return quotient == remainder
    
    
result = 0
for line in iterator:
    operation = str(line.strip())
    for item in operation.split(","):
        start = int(item.split("-")[0])
        end = int(item.split("-")[1])
        # Now we check invalid IDs in each range
        for number in range(start, end+1):
            if isInvalid(number):
                result += number

print(result)