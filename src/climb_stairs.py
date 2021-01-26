def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n):
        third = first + second
        first = second
        second = third
    return second
