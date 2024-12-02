from functools import reduce

from utils import yield_lines


class Reducer:
    increase = None
    index = 0

    def __call__(self, prev_el: str, el: str):
        prev_el, el = int(prev_el), int(el)

        if prev_el == el:
            raise Exception()

        if self.increase is None:
            self.increase = el > prev_el
        elif self.increase and el < prev_el:
            raise Exception()
        elif not self.increase and el > prev_el:
            raise Exception()
        
        if abs(el - prev_el) > 3:
            raise Exception()
        
        self.index += 1
        return el


def _process_line(line):
    line = line.split()
    r = Reducer()
    try:
        reduce(r, line)
    except Exception:
        for i in (r.index - 1, r.index, r.index + 1):
            r = Reducer()
            curr_line = list(line)
            curr_line.pop(i)
            try:
                reduce(r, curr_line)
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
