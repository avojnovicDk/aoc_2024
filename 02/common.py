from typing import Generator


def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line


class SafetyChecker:
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
