def f(s, n):
    from collections import Counter
    cnt, lo, max_l, res = Counter(), 0, 0, ''
    for hi, c in enumerate(s):
        cnt[c] += 1
        if len(cnt) <= n and (hi - lo + 1) > max_l:
            max_l = hi - lo + 1
            res = s[lo:hi + 1]
        else:
            while len(cnt) > n:
                cnt[s[lo]] -= 1
                if not cnt[s[lo]]:
                    cnt.pop(s[lo])
                lo += 1
    return res


if __name__ == '__main__':
    print(f('a', 3))
