path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day05/input.txt"

with open(path) as f:
    content = f.read().strip()

parts = content.split("\n\n")

fresh_ranges = parts[0].splitlines()
available_ids = parts[1].splitlines()

fresh_ids = [] 

for ids in available_ids:
    for ranges in fresh_ranges:
        start = int(ranges.split("-")[0])
        end = int(ranges.split("-")[1])
        if int(ids) in range(start, end+1):
            fresh_ids.append(int(ids))
            
print(len(list(set(fresh_ids))))
