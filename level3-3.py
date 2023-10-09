'''
Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks.
n will always be at least 3 (so you can have a staircase at all), but no more than 200
'''

'''
Algorithm:
Step 1: compute the n*h triangular matrix of n_stairs_max_height(n, h)
'''

def n_stairs_max_height(height, bricks):
    if bricks < 3:
        return 0
    # max height is bricks - 1
    if height > bricks - 1:
        return 0
    if height <= 1:
        return 0
    count = 0
    for h in range(2, height):
        count += n_stairs_with_height(h)
    return count

def write_lookup():
    '''
    Compute the lookup table
    :return:
    '''

def write_to_lookup(height, bricks, table):
    '''
    Adds the entry to the lookup table
    :param height:
    :param bricks:
    :return:
    '''
    table[bricks][height] = n_stairs_with_height(height, bricks)
def n_stairs_with_height(height, bricks):
    '''
    May have to add lookup for speed (use lookup if value exists, otherwise compute)
    :param height:
    :param bricks: ensure height < bricks
    :return: 0 if no valid stairs
    '''
    # base case:
    if bricks < 3:
        return 0
    # max height is bricks - 1
    if height > bricks - 1:
        return 0
    if height <= 1:
        return 0
    count = 0
    bricks_left = bricks - height
    if height > bricks // 2:
        for h in range(2, bricks):
            count += n_stairs_with_height(h, bricks_left)
        return 1 + count
    else:
        for h in range(2, height):
            count += n_stairs_with_height(h, bricks_left)
        return count
    # we lock in the first layer with height, so bricks left is bricks - height

    # 1 to account for trivial solution (height, bricks - height),
    # will not be returned by n_stairs_any_height as it is not a substair, only 1 step


def n_stairs_any_height(bricks):
    '''

    :param bricks:
    :return:
    '''
    # base case: when will
    if bricks < 3:
        return 0
    # min height is max h where T(h) <= bricks
    # min_height =
    n_stairs = 0
    for h in range(2, bricks):
        n_stairs += n_stairs_with_height(h, bricks)
    return n_stairs

# print([(i, n_stairs_any_height(i)) for i in range(5,29)])
# print(n_stairs_any_height(200))
table = [[0 for i in range(10)] for i in range(10)]
print(table[3][2])
write_to_lookup(2,3,table)
print(table[3][2])
