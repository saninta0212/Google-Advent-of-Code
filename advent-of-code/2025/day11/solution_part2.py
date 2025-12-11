# # read the text.txt file
# # then parse each line - "aaa: you hhh"
# # put them into dict stucture
# # find the key that is "you"
# # then then find the value from you and keep following for each to find path till you find out
# # then count number of paths

# from typing import Dict, List, Iterable

# def load_graph(path: str) -> Dict[str, List[str]]:
#     graph = {}
#     with open(path, 'r') as f:
#         for raw in f:
#             line = raw.strip()
#             if not line or ':' not in line:
#                 continue
#             key, rhs = line.split(':', 1)
#             key = key.strip()
#             # values separated by whitespace
#             vals = [v for v in rhs.split() if v]
#             graph[key] = vals
#     return graph

# def find_all_paths(graph: Dict[str, List[str]], start: str, goal: str) -> Iterable[List[str]]:
#     """Yield every simple path (no repeated node in path) from start to goal."""
#     stack = [(start, [start])]
#     while stack:
#         node, path = stack.pop()
#         if node == goal:
#             yield path
#             continue
#         for neigh in graph.get(node, []):
#             if neigh in path:
#                 # would form a cycle on current path — skip
#                 continue
#             stack.append((neigh, path + [neigh]))

# if __name__ == "__main__":
#     # change filename to your puzzle input file
#     graph = load_graph("/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day11/test.txt")

#     paths = list(find_all_paths(graph, "svr", "out"))
#     for p in paths:
#         print(" -> ".join(p))
#     print()
#     print("Total paths from 'you' to 'out':", len(paths))

#     # ---- new filter: paths containing both dac and fft ----
#     target1 = "dac"
#     target2 = "fft"

#     paths_with_both = [p for p in paths if target1 in p and target2 in p]

#     print(f"Paths containing both {target1!r} and {target2!r}: {len(paths_with_both)}")
#     for p in paths_with_both:
#         print(" -> ".join(p))

from typing import Dict, List
import sys
sys.setrecursionlimit(10000)

def load_graph(path: str) -> Dict[str, List[str]]:
    graph = {}
    with open(path) as f:
        for line in f:
            if ":" not in line:
                continue
            key, rhs = line.split(":", 1)
            graph[key.strip()] = rhs.split()
    return graph


def count_paths(graph: Dict[str, List[str]], start: str, goal: str, memo):
    """Count number of paths from start → goal using memoized DFS."""
    if start == goal:
        return 1
    if start in memo:
        return memo[start]

    total = 0
    for nxt in graph.get(start, []):
        total += count_paths(graph, nxt, goal, memo)

    memo[start] = total
    return total


def count_segment(graph, A, B):
    """Wrapper to avoid memo leakage between segments."""
    return count_paths(graph, A, B, memo={})


if __name__ == "__main__":
    graph = load_graph("/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day11/input.txt")

    start = "svr"
    goal = "out"

    # ---- total paths you → out ----
    total_paths = count_segment(graph, start, goal)
    print("Total routes you → out:", total_paths)

    # targets
    a = "dac"
    b = "fft"

    # ---- check direction: does dac come before fft, or the reverse? ----
    paths_you_to_a  = count_segment(graph, start, a)
    paths_you_to_b  = count_segment(graph, start, b)
    paths_a_to_b    = count_segment(graph, a, b)
    paths_b_to_a    = count_segment(graph, b, a)
    paths_a_to_out  = count_segment(graph, a, goal)
    paths_b_to_out  = count_segment(graph, b, goal)

    # ---- compute counts depending on ordering ----
    count_with_both = 0

    # case 1: you → dac → fft → out
    if paths_a_to_b > 0:
        count_with_both += paths_you_to_a * paths_a_to_b * paths_b_to_out

    # case 2: you → fft → dac → out
    if paths_b_to_a > 0:
        count_with_both += paths_you_to_b * paths_b_to_a * paths_a_to_out

    print(f"Routes containing both '{a}' and '{b}':", count_with_both)
