def romanToInt(self, s: str) -> int:
    num = 0
    i = 0
    while i < len(s):
        if s[i] == "M":
            num += 1000
        elif i < len(s) - 1 and s[i] + s[i+1] == "CM":
            num += 900
            i += 1
        elif s[i] == "D":
            num += 500
        elif i < len(s) - 1 and s[i] + s[i+1] == "CD":
            num += 400
            i += 1
        elif s[i] == "C":
            num += 100
        elif i < len(s) - 1 and s[i] + s[i+1] == "XC":
            num += 90
            i += 1
        elif s[i] == "L":
            num += 50
        elif i < len(s) - 1 and s[i]+s[i+1] == "XL":
            num += 40
            i += 1
        elif s[i] == "X":
            num += 10
        elif i < len(s) - 1 and s[i] + s[i + 1] == "IX":
            num += 9
            i += 1
        elif s[i] == "V":
            num += 5
        elif i < len(s) - 1 and s[i]+s[i + 1] == "IV":
            num += 4
            i += 1
        elif s[i] == "I":
            num += 1
        i += 1
    return num
