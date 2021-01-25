def is_happy(n: int) -> bool:
    results = {}
    result = 0

    for i in list(str(n)):
        result = int(i) * int(i) + result
    results[result] = 1

    while result != 1:
        pre = result
        result = 0
        for j in list(str(pre)):
            result = int(j) * int(j) + result
        if result in results.keys():
            return False
        else:
            results[result] = 1
    return True


print(is_happy(2))