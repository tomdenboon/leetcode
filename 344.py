def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[len(s) - (i + 1)] = s[len(s) - (i + 1)], s[i]
