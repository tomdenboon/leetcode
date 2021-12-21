def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    upper = 2 ** 31
    lower = -1 * upper
    v = 1
    if '-' == s[0]:
        v = -1
        s = s[1:]
    elif '+' == s[0]:
        s = s[1:]
    dig_str = ""
    for c in s:
        if c.isdigit():
            dig_str += c
        else:
            break
    if not dig_str:
        return 0
    v *= int(dig_str)
    if v < lower:
        return lower
    if v > upper - 1:
        return upper - 1
    return v
