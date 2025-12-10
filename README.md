# Google Advent of Code

[![Advent of Code](https://img.shields.io/badge/Advent%20of%20Code-2025-blue)](https://adventofcode.com/)  
[![Python](https://img.shields.io/badge/Python-3.11-green)](https://www.python.org/)  
[![Progress](https://img.shields.io/badge/Progress-33%25-blue)](#daily-challenges)

This repository contains my solutions for **[Advent of Code](https://adventofcode.com/)** challenges. Each puzzle tests problem-solving, algorithmic thinking, and creative coding in Python (and potentially other languages).  

I track my progress with day-wise badges and keep well-documented solutions for learning and reference.

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Daily Challenges](#daily-challenges)  
- [References](#references)  
- [Contributing](#contributing)  

---

## Project Structure

```
advent-of-code/
│
├── 2025/
│   ├── day01/
│   │   ├── solution.py
│   │   ├── input.txt
│   │   └── README.md
│   ├── day02/
│   │   └── ...
│   └── utils/
│       └── helpers.py
│
├── README.md
└── requirements.txt
```

---

## Installation

1. Clone the repository:

```bash
git https://github.com/saninta0212/Google-Advent-of-Code.git
cd advent-of-code
```

2. (Optional) Set up a virtual environment:

```bash
python -m venv gaoc
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Most solutions rely on Python standard library; extras will be listed in `requirements.txt`.

---

## Usage

Run the solution for a given day:

```bash
cd google_aoc_2025/advent-of-code/2025
python -m day01.solution_part2
```

Add any utility functions in `utils/helpers.py` to reuse across multiple days.

---

## Daily Challenges

| Day | Title | Status | Language | Notes |
|-----|-------|--------|---------|-------|
| 01  | Secret Entrance | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | mod operations are cool |
| 02  | Gift Shop | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | mod operations are cool pt 2 |
| 03  | Lobby | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | being greedy makes you faster |
| 04  | Printing Department | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | Pruning trees |
| 05  | Cafeteria | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | Merge Sort |
| 06  | Trash Compactor | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | Array iteration |
| 07  | Laboratories | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | Recursion & Memoization|
| 08  | Playground | ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | Bruh what is this union find structure?? I barely passed 320 |
| 09  |  Movie Theater | ![In Progress](https://img.shields.io/badge/✓-Completed-brightgreen) | Python | kinda hit a wall on pt 2 |

> Status key:  
> ![Completed](https://img.shields.io/badge/✓-Completed-brightgreen) Completed  
> ![In Progress](https://img.shields.io/badge/⚠️-In_Progress-yellow) In Progress  
> ⬜ Pending  

---

## References

- **[Advent of Code Official Website](https://adventofcode.com/)**  
- **[Python Standard Library](https://docs.python.org/3/library/)**   
- **[PEP 8 – Python Style Guide](https://pep8.org/)**  

---

## Contributing

- Fork the repository.  
- Create a branch: `git checkout -b feature/day01-optimization`  
- Submit a pull request with detailed notes.  

---

## Notes / Future Work
