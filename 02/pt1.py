from functools import reduce

from common import SafetyChecker, yield_lines


def solve(file_path: str) -> int:
    safe_count = 0
    for line in yield_lines(file_path):
        check = SafetyChecker()
        try:
            reduce(check, line.split())
        except Exception:
            pass
        else:
            safe_count += 1
            
    return safe_count


assert solve("example1.txt") == 2
assert solve("input.txt") == 230
