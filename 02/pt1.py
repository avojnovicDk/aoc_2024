from functools import reduce

from utils import yield_lines


class Reducer:
    increase = None

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
        
        return el

def solve(file_path: str) -> int:
    safe_count = 0
    for line in yield_lines(file_path):
        r = Reducer()
        try:
            reduce(r, line.split())
        except Exception:
            pass
        else:
            safe_count += 1
            
    return safe_count


assert solve("example1.txt") == 2
assert solve("input.txt") == 230
