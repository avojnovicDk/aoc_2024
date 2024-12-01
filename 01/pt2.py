from collections import Counter
from typing import Generator

from utils import yield_lines


def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def solve(file_path: str) -> int:
    col1, col2 = list(), list()
    for line in yield_lines(file_path):
        v1, v2 = line.split()
        col1.append(int(v1))
        col2.append(int(v2))
    
    col1, col2 = Counter(col1), Counter(col2)
    
    return sum(n * count * col2[n] for n, count in col1.items())


assert solve("example1.txt") == 31
assert solve("input.txt") == 25358365