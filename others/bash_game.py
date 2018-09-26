# 总共有n个，每次最多取m个，先取光者胜
def bash_game(n, m):
    return n % (m + 1) != 0


# 总共有n个，每次最多取m个，先取光者输
def bash_game1(n, m):
    return (n - 1) % (m + 1) != 0

