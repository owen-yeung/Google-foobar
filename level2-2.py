def solution(xs):
    xs.sort()
    if len(xs) == 1 and xs[0] < 0:
        return xs[0]
    negs, pos = split(xs)
    if len(negs) == 0 and len(pos) == 0:
        return 0
    elif len(negs) == 1 and len(pos) == 0:
        return 0
    else:
        if len(negs) % 2 == 1:
            negs = negs[:-1]
        return str(prod(negs) * prod(pos))
# return product of everything in xs, 1 if empty
def prod(xs):
    res = 1
    for x in xs:
        res *= x
    return res
# split sorted list xs into a list of negatives and positives
def split(xs):
    while xs.count(0) > 0:
        xs.remove(0)
    if len(xs) == 0:
        return [], []
    elif xs[0] > 0:
        return [], xs
    elif xs[-1] < 0 :
        return xs, []
    for i in range(len(xs)):
        n = xs[i]
        if n > 0:
            return xs[:i], xs[i:]

print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([-1]))
print(solution([-1,-2,-3,-4,-5]))
print(solution([-1,0,0,0,0]))