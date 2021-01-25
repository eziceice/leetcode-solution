from typing import List


def generate(rows: int) -> List[List[int]]:
    if rows == 0:
        return []
    if rows == 1:
        return [[1]]
    if rows == 2:
        return [[1], [1, 1]]
    outer = [[1], [1, 1]]
    for i in range(3, rows + 1):
        inner = []
        for j in range(i):
            if j == 0:
                inner.append(1)
            elif j == i - 1:
                inner.append(1)
            else:
                inner.append(outer[i-2][j] + outer[i-2][j-1])
        outer.append(inner)
    return outer


