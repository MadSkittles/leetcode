#两堆物品分别为x和y个，从一堆去任意个或者从两堆取相同个，先取光者胜
def wythoff_game(x, y):
    x, y = min(x, y), max(x, y)
    return x != int((5 ** 0.5 + 1) / 2 * (y - x))

