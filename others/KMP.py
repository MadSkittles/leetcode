def kmp(s, p):
    next, k = [-1] * len(p), -1
    for i, c in enumerate(p):
        while k > -1 and s[k + 1] != c:
            k = next[k]
        if s[k + 1] == c:
            k += 1
        next[i] = k
    k = -1
    for i, c in enumerate(s):
        while k > -1 and p[k + 1] != c:
            k = next[k]
        if p[k + 1] == c:
            k += 1
        if k == len(p) - 1:
            return i - len(p) + 1
    return -1


if __name__ == '__main__':
    print(kmp('helloworld', 'world'))
    print(kmp('helloworld', 'rorld'))
