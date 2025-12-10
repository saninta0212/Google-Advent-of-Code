path = "/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day09/input.txt"
with open(path) as f:
    tiles = f.read().split("\n")

areas = []

def calc_area(x1,y1,x2,y2):
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)
    
for i in range(0, len(tiles)):
    for j in range(i+1, len(tiles)):
        x1,y1 = tiles[i].split(",")
        x2,y2 = tiles[j].split(",")
        area = calc_area(int(x1),int(y1),int(x2),int(y2))
        areas.append(area)
print(max(areas))