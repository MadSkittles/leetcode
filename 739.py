class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                p, pt = stack.pop()
                res[p] = i - p
            stack.append((i, t))
        return res