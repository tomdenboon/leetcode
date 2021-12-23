def countPoints(self, rings: str) -> int:
    r = []
    for _ in range(10):
        r.append({'R': False, 'G': False, 'B': False})
    i = 0
    while i < len(rings):
        r[int(rings[i+1])][rings[i]] = True
        i += 2
    total = 0
    for i in r:
        print(i)
        yes = True
        for rgb in i:
            if not i[rgb]:
                yes = False
                break
        if yes:
            total += 1

    return total
