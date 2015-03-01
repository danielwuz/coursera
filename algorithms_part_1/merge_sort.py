from random import uniform
from pylab import plot, show


def merge_sort(nums):
    if len(nums) <= 10:
        return sorted(nums)
    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)


def merge(left, right):
    m, n = len(left), len(right)
    merged = [0] * (m + n)
    i, j = 0, 0
    for k in range(m + n):
        if j == n or (i < m and left[i] < right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
    return merged


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def polar_order(self, q1, q2):
        dy1 = q1.y - self.y
        dy2 = q2.y - self.y

        if dy1 == 0 and dy2 == 0:
            # vertically
            return 0
        elif dy1 >= 0 and dy2 < 0:
            # q1 above current point; q2 below
            return -1
        elif dy2 >= 0 and dy1 < 0:
            return 1
        else:
            return -Point.ccw(self, q1, q2)

    @staticmethod
    def ccw(a, b, c):
        area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if area < 0:
            return 1
        elif area > 0:
            return 1
        else:
            return 0

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)


def generate_point():
    return Point(uniform(-1, 1) * 100, uniform(-1, 1) * 100)


points = {generate_point() for _ in range(10)}


def myplot():
    x = [p.x for p in points]
    y = [p.y for p in points]
    plot(x, y, 'o', (0,), (0,), 'rx')
    show()


# myplot()
