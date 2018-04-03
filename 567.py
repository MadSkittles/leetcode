class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        cnt1, cnt2 = {k: 0 for k in 'abcdefghijklmnopqrstuvwxyz'}, {k: 0 for k in 'abcdefghijklmnopqrstuvwxyz'}
        for i in range(len(s1)):
            cnt1[s1[i]] += 1
            cnt2[s2[i]] += 1
        lo, hi = 0, len(s1)
        while hi < len(s2):
            if cnt1 == cnt2:
                return True
            cnt2[s2[lo]] -= 1
            cnt2[s2[hi]] += 1
            lo += 1
            hi += 1
        return cnt1 == cnt2