import math
import random


class Solution:
    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        r = random.triangular(0, self.r, self.r)
        theta = random.uniform(-math.pi, math.pi)
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]


if __name__ == "__main__":
    solution = Solution(1, 0, 0)
    print(solution.randPoint())
    print(solution.randPoint())
    print(solution.randPoint())
