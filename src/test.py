def testfunc():
    x = [0, 1, 2]
    for t in x:
        yield (t ** index for index in range(3))


print(*zip(*testfunc()))
print(*zip(*map(list, testfunc())))
