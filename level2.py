def solution(l):
    # Your code here
    tuples = []
    res = []
    for s in l:
        tuples.append(str_to_tuple(s))
    sorted_tuples = sorted(tuples)
    for t in sorted_tuples:
        res.append(tuple_to_str(t))
    return res


def str_to_tuple(version):
    tiers = version.count('.')
    res_list = []
    while tiers > 0:
        dot_index = version.index('.')
        res_list.append(int(version[:dot_index]))
        version = version[dot_index + 1:]
        tiers -= 1
    res_list.append(int(version))
    return tuple(res_list)

def tuple_to_str(tup):
    tiers = len(tup)
    res = ""
    for t in range(tiers): #hoping this just exits with empty range
        res += str(tup[t]) + "."
    return res[:-1]

'''
Input:
solution.solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
Output:
    0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

Input:
solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
Output:
    1.0,1.0.2,1.0.12,1.1.2,1.3.3
'''
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
# print(sorted([(1,1,2), (1,0), (1,3,3), (1,0,12), (1,0,2), (1,)]))