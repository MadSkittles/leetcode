class Solution:
    def lexicalOrder(self, n):
        stack, res = [], []
        start = 1
        while len(res) < n:
            if start <= n:
                res.append(start)
                stack.append(start)
                start *= 10
            else:
                start = stack.pop()
                while start % 10 == 9:
                    start = stack.pop()
                start += 1
        return res

    def lexicalOrder1(self, n):
        self.n = n
        self.res = []
        for i in range(1, 10):
            self.f(i)
        return self.res

    def f(self, base):
        if base > self.n:
            return
        self.res.append(base)
        for i in range(0, 10):
            self.f(base * 10 + i)
