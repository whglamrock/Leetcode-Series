
from bisect import bisect_left, bisect_right

class RangeModule:

    def __init__(self):
        # X stores all left & right boundaries; e.g. [[left, right), [left, right), ...]
        self.X = []

    def addRange(self, left, right):
        # number of all x values < left (excluding =)
        i = bisect_left(self.X, left)
        # number of all x values <= right
        j = bisect_right(self.X, right)

        # run 4 conditions (1 & 3, 2 & 3, 1 & 4, 2 & 4) and see what X[i:j] refers to
            # 1) i % 2 == 0: even num of x values < left; add left to the boundaries
            # 2) j % 2 == 0: even num of x values <= right; add right to boundaries
            # 3) i % 2 != 0: odd num of x values < left; left is within one current range
            # 4)  j % 2 != 0: odd num of x values <= right; right is within one current range
        self.X[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    # for queryRange to return True, [left, right) has to completely fall into one of the ranges
    def queryRange(self, left, right):
        i = bisect_right(self.X, left)
        j = bisect_left(self.X, right)
        return i == j and i % 2 == 1

    def removeRange(self, left, right):
        i = bisect_left(self.X, left)
        j = bisect_right(self.X, right)
        self.X[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)

