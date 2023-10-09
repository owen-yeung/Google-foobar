'''
Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks.
n will always be at least 3 (so you can have a staircase at all), but no more than 200
'''

'''
Observations:
- for n bricks, (n-1, 1) is always a staircase
n_staris_with_height(n-2, n) = 1 + sol(2) ([n-2, 2] + sol(2))
(n-3,3) (n-3, 2, 1) = (n-3,3) + sol(3)
(n-4, 4) (n-4, 3, 1) = (n-4, 4) + sol(4)
.
.
.
n_staris_with_height(n-x, n) = 1 + sol(x)
.
.
.
* Holds for increasing x until n - x = x + 1 or x + 2
* What about for max height < n / 2 ?
* (we must move bricks from the second highest step to maintain staircase validity)
* Can only be moved to a step that's 2 larger than the next step
* IDEA: function returns number of staircases WITH HEIGHT = x
.
.
.

'''

'''
Brainstorm:
suppose for some A i know solution(A)
Then I know solution(2A+1) with max height A+1
max height A+2: solution (A-1)
max height A+3: solution(A-2) (actually no, I can move bricks in front)
.
.
.

'''

def n_stairs_with_height(height, bricks):
    '''

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

print([(i, n_stairs_any_height(i)) for i in range(5,29)])
# print(n_stairs_any_height(200))
