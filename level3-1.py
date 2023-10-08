
def solution(x, y):
    return tostr(last_step(int(x), int(y)))

def tostr(n):
    if n == ninf:
        return 'impossible'
    else:
        return str(n)
def last_step(x, y):
    '''Should return the number of cycles, if not impossible'''
    # handle special cases
    ninf = -float("inf")
    if x < 1 or y < 1:
        return ninf
    elif x == 1:
        return y - 1
    elif y == 1:
        return x - 1
    elif x % y == 0 or y % x == 0:
        return ninf
    else:
        # lol this can probably be written more elegantly but whatever
        if y > 2 * x:
            used_y = ninf
            skip_gens = y // x - 1
            used_x = skip_gens + last_step(x, y - skip_gens * x) - 1
        elif x > 2 * y:
            used_x = ninf
            skip_gens = x // y - 1
            used_y = skip_gens + last_step(x - skip_gens * y, y) - 1
        elif y > x:
            used_x = last_step(x, y - x)
            used_y = ninf
        elif x > y:
            used_y = last_step(x - y, y)
            used_x = ninf
        x_inf = used_x == ninf
        y_inf = used_y == ninf
        if x_inf and y_inf:
            return ninf
        elif (not x_inf) and (not y_inf):
            return min(used_x, used_y) + 1
        elif x_inf:
            return used_y + 1
        elif y_inf:
            return used_x + 1
        else:
            raise NotImplementedError

print(solution(4, 7))