from utils.helpers import read_input


### This solution is in O(n2)
path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day03/input.txt"
iterator = read_input(path)

def find_k_largest(bank, k):
    num = k
    length_bank = len(bank)
    i = 0
    jolt = ""
    
    while num > 0:
        window_to_check = length_bank - (num-1)
        max_battery = 0
        for index, battery in enumerate(bank[i:window_to_check]):
            if battery > max_battery:
                max_battery = battery
                i = index
        jolt += str(max_battery)
        i += 1
        num -= 1
        
    print(jolt)
    return int(jolt)

joltage = 0
for bank in iterator:
    batteries = [int(x) for x in str(bank.strip())] 
    joltage += find_k_largest(batteries, 2)
    
print(joltage)