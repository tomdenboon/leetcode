def longestValidParentheses(s):
    stack = []
    p_map = [0] * len(s)
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif stack:
            prev_i = stack.pop()
            p_map[prev_i] = 1
            p_map[i] = 1
    longest = 0
    streak = 0
    for p in p_map:
        if p:
            streak += 1
        else:
            longest = max(streak, longest)
            streak = 0
    return max(streak, longest)
