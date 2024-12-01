from typing import Generator


def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line
