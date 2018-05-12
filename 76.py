class Solution:
    def minWindow(self, s, t):
        if len(t) == 1:
            return t if t in s else ''
        from collections import Counter
        t, cnt = Counter(t), {c: 0 for c in t}
        lo, hi, min_length, res_lo, res_hi = 0, 0, float('inf'), 0, 0
        lo = hi = 0
        while lo < len(s) and s[lo] not in cnt:
            lo = hi = lo + 1
        while lo <= hi < len(s):
            if s[hi] in cnt:
                cnt[s[hi]] += 1
                if all(cnt[k] >= t[k] for k in cnt):
                    if hi - lo + 1 < min_length:
                        min_length, res_lo, res_hi = hi - lo + 1, lo, hi
                    cnt[s[lo]] -= 1
                    lo += 1
                    while lo < len(s) and s[lo] not in cnt:
                        lo += 1
                    cnt[s[hi]] -= 1
                    hi -= 1
            hi += 1
        return s[res_lo:res_hi + 1] if min_length != float('inf') else ''


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("aabAA",
                             "BB"))
