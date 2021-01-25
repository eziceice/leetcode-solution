def hamming_weight(n: int) -> int:
    result = bin(n).count('1')
    return result
