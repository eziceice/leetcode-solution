def roman_to_int(s: str) -> int:
    roman_integers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_integers.keys():
            result = result + roman_integers[s[i:i+2]]
            i = i + 2
        else:
            result = result + roman_integers[s[i]]
            i = i + 1
    return result


print(roman_to_int('IV'))