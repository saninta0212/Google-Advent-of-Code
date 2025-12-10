from utils.helpers import read_input
from collections import Counter

path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day08/input.txt"
junction = read_input(path)

# Parse junction box positions
box_positions = [tuple(map(int, line.strip().split(','))) for line in junction if line.strip()]
n = len(box_positions)

def calc_distance_sq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

# Build all pairwise edges with squared distances
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = calc_distance_sq(box_positions[i], box_positions[j])
        edges.append((d, i, j))

edges.sort()  # sort by distance

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

dsu = DSU(n)

# Only connect the 1000 closest pairs (or fewer if not enough edges)
# connections = 0
# for _, i, j in edges:
#     if dsu.union(i, j):
#         connections += 1
#     if connections == 1000:
#         break
pairs_to_connect = edges
for _, i, j in pairs_to_connect:
    dsu.union(i, j)  # DSU still updates circuits

# Count the size of each circuit
root_list = [dsu.find(i) for i in range(n)]
counts = Counter(root_list)
sizes = sorted(counts.values(), reverse=True)

# Multiply top 3 largest circuits
if len(sizes) < 3:
    result = None
else:
    result = sizes[0] * sizes[1] * sizes[2]

print("Top 3 circuit sizes:", sizes[:3])
print("Product:", result)
