def longestCommonPrefix(strs):
    c = ""
    for s in zip(*strs):
        if len(set(s)) == 1:
            c += s[0]
        else:
            break
    return c
