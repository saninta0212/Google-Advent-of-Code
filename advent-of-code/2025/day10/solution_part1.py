import re
import numpy as np
from itertools import product

def parse_line(line):
    """Parse a machine line to extract target state and button configurations."""
    # Extract indicator light diagram
    bracket_match = re.search(r'\[([.#]+)\]', line)
    if not bracket_match:
        return None
    
    target = [1 if c == '#' else 0 for c in bracket_match.group(1)]
    
    # Extract button wiring schematics
    paren_matches = re.findall(r'\(([0-9,]+)\)', line)
    buttons = []
    for match in paren_matches:
        buttons.append([int(x.strip()) for x in match.split(',')])
    
    return target, buttons

def solve_gf2_all_solutions(matrix, target):
    """Find all solutions to a system of linear equations over GF(2)."""
    rows, cols = matrix.shape
    
    # Create augmented matrix
    aug = np.hstack([matrix.copy(), target.reshape(-1, 1)])
    
    # Track which columns have pivots
    pivot_cols = []
    pivot_row = 0
    
    # Gaussian elimination over GF(2)
    for col in range(cols):
        if pivot_row >= rows:
            break
        
        # Find pivot
        found = False
        for row in range(pivot_row, rows):
            if aug[row, col] == 1:
                # Swap rows
                aug[[pivot_row, row]] = aug[[row, pivot_row]]
                found = True
                break
        
        if not found:
            continue
        
        pivot_cols.append(col)
        
        # Eliminate
        for row in range(rows):
            if row != pivot_row and aug[row, col] == 1:
                aug[row] = (aug[row] + aug[pivot_row]) % 2
        
        pivot_row += 1
    
    # Check for inconsistency
    for row in range(rows):
        if np.all(aug[row, :-1] == 0) and aug[row, -1] == 1:
            return None  # No solution
    
    # Find free variables (columns without pivots)
    free_vars = [i for i in range(cols) if i not in pivot_cols]
    
    if not free_vars:
        # Unique solution - back substitution
        solution = np.zeros(cols, dtype=int)
        for row in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[row]
            val = aug[row, -1]
            for c in range(col + 1, cols):
                val = (val + aug[row, c] * solution[c]) % 2
            solution[col] = val
        return [solution]
    
    # Multiple solutions - enumerate all combinations of free variables
    solutions = []
    for free_values in product([0, 1], repeat=len(free_vars)):
        solution = np.zeros(cols, dtype=int)
        
        # Set free variables
        for i, var in enumerate(free_vars):
            solution[var] = free_values[i]
        
        # Back substitution for pivot variables
        for row in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[row]
            val = aug[row, -1]
            for c in range(col + 1, cols):
                val = (val + aug[row, c] * solution[c]) % 2
            solution[col] = val
        
        solutions.append(solution)
    
    return solutions

def solve_machine(target, buttons):
    """Find minimum button presses to configure a machine."""
    num_lights = len(target)
    num_buttons = len(buttons)
    
    # Build matrix where matrix[i][j] = 1 if button j toggles light i
    matrix = np.zeros((num_lights, num_buttons), dtype=int)
    
    for j, button in enumerate(buttons):
        for light in button:
            if light < num_lights:
                matrix[light, j] = 1
    
    target_array = np.array(target, dtype=int)
    solutions = solve_gf2_all_solutions(matrix, target_array)
    
    if solutions is None:
        return None
    
    # Find solution with minimum number of button presses
    min_presses = float('inf')
    for solution in solutions:
        presses = np.sum(solution)
        min_presses = min(min_presses, presses)
    
    return min_presses

def main():
    """Read input.txt and solve all machines."""
    try:
        with open('/Users/sambina/Documents/google_aoc_2025/advent-of-code/2025/day10/input.txt', 'r') as f:
            lines = f.readlines()
        
        total_presses = 0
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
            
            parsed = parse_line(line)
            if not parsed:
                print(f"Machine {i}: Could not parse line")
                continue
            
            target, buttons = parsed
            presses = solve_machine(target, buttons)
            
            if presses is None:
                print(f"Machine {i}: No solution found")
            else:
                print(f"Machine {i}: {presses} presses (target: [{''.join('#' if x else '.' for x in target)}])")
                total_presses += presses
        
        print(f"\n{'='*50}")
        print(f"Total button presses required: {total_presses}")
        print(f"{'='*50}")
        
    except FileNotFoundError:
        print("Error: input.txt not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test with the examples first
    test_data = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    ]
    
    print("Testing with examples:")
    print("="*50)
    test_total = 0
    for i, line in enumerate(test_data, 1):
        parsed = parse_line(line)
        if parsed:
            target, buttons = parsed
            presses = solve_machine(target, buttons)
            print(f"Machine {i}: {presses} presses (target: [{''.join('#' if x else '.' for x in target)}])")
            test_total += presses
    
    print(f"\nTest total: {test_total} (expected: 7)")
    print("="*50)
    print()
    
    # Now run on actual input
    main()