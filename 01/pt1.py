from utils import yield_lines


def solve(file_path: str) -> int:
    col1, col2 = list(), list()
    for line in yield_lines(file_path):
        v1, v2 = line.split()
        col1.append(int(v1))
        col2.append(int(v2))
    return sum(abs(b - a) for a, b in zip(sorted(col1), sorted(col2)))


assert solve("example1.txt") == 11
assert solve("input.txt") == 2580760
