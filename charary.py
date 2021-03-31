"""
Library to convert number with base system borrowing characters:
'a' -> 10
'b' -> 11
...
'z' -> 35
"""

import math

def charary_to_decimal(c):
    """
        Converts base-36 single digit to decimal.
        Only unsigned numbers
    """
    if c.isdigit():
        return int(c)
    # Assuming c is character order from "a"
    return 10 + (ord(c.lower()) - ord('a'))

def charary_str_2_dec(s):
    """
        Converts each char in string of base-32 to base-10
        Only unsigned.
    """
    retval = 0
    digit_index = 0
    for c in reversed(s):
        dec = (charary_to_decimal(c))
        retval += (dec * (10 ** digit_index))
        digit_index += int(math.log10(dec)) + 1 if dec > 0 else 1
    return retval


if __name__ == "__main__":
    print(charary_str_2_dec("zero"))
