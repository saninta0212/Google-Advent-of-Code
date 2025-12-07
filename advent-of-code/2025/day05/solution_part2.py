path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day05/input.txt"

with open(path) as f:
    content = f.read().strip()

parts = content.split("\n\n")
fresh_ranges = parts[0].splitlines()

# Parse and sort intervals
intervals = []
for ranges in fresh_ranges:
    start, end = map(int, ranges.split("-"))
    intervals.append((start, end))

intervals.sort()  # Sort by start position

# Merge overlapping intervals
merged = []
for start, end in intervals:
    if merged and start <= merged[-1][1] + 1:
        # Check if the start of this range is less than end of the previous range 
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        # Non-overlapping - add as new interval
        merged.append((start, end))

# Count total IDs across all merged intervals
total = sum(end - start + 1 for start, end in merged)
print(total)