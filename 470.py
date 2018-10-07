import random


class Solution:
    def rand10(self):
        return 5 * self.rand1() + self.rand5()

    def rand5(self):
        rnd = rand7()
        while rnd >= 6:
            rnd = rand7()
        return rnd

    def rand1(self):
        rnd = rand7()
        while rnd == 7:
            rnd = rand7()
        return rnd % 2


def rand7():
    return random.randint(1, 7)

