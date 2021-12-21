def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    sol = []
    interval = numRows * 2 - 2
    for i in range(numRows):
        sol.append("")
    row = 0
    for i in range(len(s)):
        row = row % interval
        if row < numRows:
            sol[row] += s[i]
        else:
            sol[numRows-2 - (row - numRows)] += s[i]
        row += 1
    return "".join(sol)
