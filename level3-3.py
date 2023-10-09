'''
Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks.
n will always be at least 3 (so you can have a staircase at all), but no more than 200
'''

import numpy as np
class Stair_calculator:
    max_bricks = 200
    def __init__(self):
        self.table = -np.ones((self.max_bricks + 1, self.max_bricks + 1), np.int_)

    def write_entry(self, height, bricks, val):
        '''
        Adds the entry to the lookup table
        :param height:
        :param bricks:
        :return:
        '''
        self.table[height][bricks] = val

    def fill_table(self):
        for bricks in range(3, Stair_calculator.max_bricks + 1):
            for height in range(2, bricks):
                self.n_stairs_with_height(height, bricks)

    def n_stairs_with_height(self, height, bricks):
        if bricks < 3:
            return 0
        # max height is bricks - 1
        if height > bricks - 1:
            return 0
        if height <= 1:
            return 0
        if self.in_table(height, bricks):
            return self.get_entry(height, bricks)
        count = 0
        bricks_left = bricks - height
        if height > bricks // 2:
            count = 1
            for h in range(2, bricks):
                count += self.n_stairs_with_height(h, bricks_left)
        else:
            for h in range(2, height):
                count += self.n_stairs_with_height(h, bricks_left)
        self.write_entry(height, bricks, count)
        return count

    def in_table(self, height, bricks):
        return self.table[height][bricks] >= 0

    def get_entry(self, height, bricks):
        return self.table[height][bricks]

    def n_stairs_any_height(self, bricks):
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
            n_stairs += self.n_stairs_with_height(h, bricks)
        return n_stairs

def solution(n):
    s = Stair_calculator()
    return s.n_stairs_any_height(n)
