'''
Challenge: Return number of triples (a,b,c) in a list that satisfy c % b == 0 and b % a == 0
'''
'''
raw: 
1,2,3,4,5,6
number of prev items divisible:
0,1,1,2,1,3
number of triples:
0,0,0,1,0,2

raw: 
1,2,4,8,16,32
number of prev items divisible:
0,1,2,3,4,5
number of triples:
0,0,1,3,6,10

raw: 
1,1,1,1,2,6,8,12
number of prev items divisible:
0,1,2,3,4,5,5,6
number of triples:
0,0,1,3,...
'''
# probably not a runtime problem? there exists a "took too long" error

def num_pairs(l):
    '''
    :param l: list of ints between 1-999999
    :return: list x where x[i] = of how many prev numbers of l[i] are divisible
    '''
    length = len(l)
    num_pairs = length * [0]
    for i in range(length):
        for j in range(i):
            if l[i] % l[j] == 0:
                num_pairs[i] += 1
    return num_pairs

def num_triples(l, num_pairs):
    '''
    If l[i] % l[j] == 0: add num_pairs[j] to num_triples[i]
    :param l:
    :return: list x where x[i] is sum of num_pair counts of all divisible prev x[j]
    '''
    length = len(l)
    num_triples = length * [0]
    for i in range(length):
        for j in range(i):
            if l[i] % l[j] == 0:
                num_triples[i] += num_pairs[j]
    return num_triples

def solution(l):
    return sum(
        num_triples(l, num_pairs(l))
    )

print(solution([44] * 1000 + [55] * 1000))
