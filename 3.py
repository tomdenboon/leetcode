def lengtOfLongestSubstring(s):
    sub = ""
    longest_sub = 0
    for c in s:
        j = sub.find(c) + 1
        sub = sub[j:] + c
        if len(sub) > longest_sub:
            longest_sub = len(sub)
    return longest_sub
