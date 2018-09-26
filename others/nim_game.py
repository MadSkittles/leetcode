from functools import reduce


# 共有n堆，每堆有a1、a2...an个，每次在一堆中至少取一个，先取光者输
def nim_game(heaps):
    return reduce(lambda x, y: x ^ y, heaps) != 0

