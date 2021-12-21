def reverse(x):
    rev = str(x)[::-1]
    if rev[-1] == '-':
        rev = '-' + rev[:-1]
    res = int(rev)
    if (-1*2 ** 31 < res < 2 ** 31):
        return res
    return 0
