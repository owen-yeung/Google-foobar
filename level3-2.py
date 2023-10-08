'''
Challenge: Return number of triples (a,b,c) in a list that satisfy c % b == 0 and b % a == 0
'''

# probably not a runtime problem? there exists a "took too long" error
def solution(l):
    '''
    algorithm: work backwards from the list
    let z = last item
    extract all ints that divide z
    count number of lucky triples with z
    remove z from list and repeat
    (May have to count and trip 1s for recursion depth)
    '''
    if len(l) < 3:
        return 0
    count = 0
    while len(l) >= 3:
        z = l[-1]
        l = l[:-1]
        div_z = []
        for x in l:
            if z % x == 0:
                div_z.append(x)
        count += num_pairs(div_z)
    return count
def num_pairs(lst):
    '''
    Take a list of ints that divide z
    :return: number of pairs s.t. lst[i]|lst[j] and i<j
    algorithm:
    - start from last item
    - loop through list and check for divis
    - go to the next last item
    - end at first item
    '''

    count = 0
    # catch ones
    # generalize: if there's a number that divides every number behind,
    oneless = []
    length = len(lst)
    for i in range(length):
        if lst[i] == 1:
            count += length - i - 1
        else:
            oneless.append(lst[i])
    lst = oneless
    length = len(lst)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if lst[i] % lst[j] == 0:
                count += 1
    return count

# print(solution(range(1, 2000)))
# print([solution([1] * i) for i in range(3, 20)])
l = [1,2,3]
print(l[:-1])
# print(solution([1, 2, 3, 4, 5, 6]), solution([1,1,1]))

# Check mutating list

