from functools import reduce

from common import SafetyChecker, yield_lines


def _process_line(line):
    line = line.split()
    check = SafetyChecker()
    try:
        reduce(check, line)
    except Exception:
        for i in (check.index - 1, check.index, check.index + 1):
            check = SafetyChecker()
            curr_line = list(line)
            curr_line.pop(i)
            try:
                reduce(check, curr_line)
            except Exception:
                pass
            else:
                return True
    else:
        return True
    
    return False


def solve(file_path: str) -> int:
    safe_count = 0
    for line in yield_lines(file_path):
        if _process_line(line):
            safe_count += 1

    return safe_count


assert solve("example1.txt") == 4
assert solve("input.txt") == 301
