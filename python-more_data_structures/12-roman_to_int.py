#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_vals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev = 0
    for char in reversed(roman_string):
        val = roman_vals.get(char, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total
