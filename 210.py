def findOrder(numCourses, prerequisites):
    scheduler = {}
    preq = [0] * numCourses
    for pair in prerequisites:
        if pair[1] in scheduler:
            scheduler[pair[1]].append(pair[0])
        else:
            scheduler[pair[1]] = [pair[0]]
        preq[pair[0]] += 1

    schedule = []
    for i in range(numCourses):
        if preq[i] == 0:
            schedule.append(i)

    f_schedule = []
    while schedule:
        s = schedule.pop(0)
        f_schedule.append(s)
        if s in scheduler:
            compl = scheduler[s]
            for c in compl:
                preq[c] -= 1
                if preq[c] == 0:
                    schedule.append(c)
    if len(f_schedule) < numCourses:
        return []
    return f_schedule
