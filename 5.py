def longestPalindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i > len(longest):
                pal = s[i:j]
                rev_pal = s[i:j][::-1]
                if pal == rev_pal:
                    longest = pal
    return longest
