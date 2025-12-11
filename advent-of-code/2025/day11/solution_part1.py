# read the text.txt file
# then parse each line - "aaa: you hhh"
# put them into dict stucture
# find the key that is "you"
# then then find the value from you and keep following for each to find path till you find out
# then count number of paths

from typing import Dict, List, Iterable

def load_graph(path: str) -> Dict[str, List[str]]:
    graph = {}
    with open(path, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line or ':' not in line:
                continue
            key, rhs = line.split(':', 1)
            key = key.strip()
            # values separated by whitespace
            vals = [v for v in rhs.split() if v]
            graph[key] = vals
    return graph

def find_all_paths(graph: Dict[str, List[str]], start: str, goal: str) -> Iterable[List[str]]:
    """Yield every simple path (no repeated node in path) from start to goal."""
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == goal:
            yield path
            continue
        for neigh in graph.get(node, []):
            if neigh in path:
                # would form a cycle on current path — skip
                continue
            stack.append((neigh, path + [neigh]))

if __name__ == "__main__":
    # change filename to your puzzle input file
    graph = load_graph("/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day11/input.txt")

    paths = list(find_all_paths(graph, "you", "out"))
    for p in paths:
        print(" -> ".join(p))
    print()
    print("Total paths from 'you' to 'out':", len(paths))
