def mortal_rabbit(n: int, m: int):
    history = [0] * m
    history[0], history[1] = 0, 1
    for x in range(2, n):
        copy = list(history)
        history[0] = sum(history[1:])
        for y in range(1, m):
            history[y] = copy[y - 1]
    return sum(history)

print(mortal_rabbit(98, 19))




#print(mortal_rabbit(99, 17))