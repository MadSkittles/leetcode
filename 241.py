class Solution:
    def diffWaysToCompute(self, input: str):
        self.args_set = set()
        nums, args = '', []
        for i, c in enumerate(input):
            if c in '+-*':
                args.append(nums)
                nums = ''
                args.append(c)
            elif c.isdigit():
                nums += c
                if i == len(input) - 1:
                    args.append(nums)
        return list(map(lambda x:eval(str(x).replace('\'', '').replace(',', '')),self.f(args)))

    def f(self, args):
        if len(args) == 1:
            return args[0],

        exp = tuple(args)
        if exp in self.args_set:
            return ()
        else:
            self.args_set.add(exp)

        res = []
        for i, c in enumerate(args):
            if c in '+-*':
                res.extend(self.f(args[:i - 1] + [(args[i - 1], c, args[i + 1])] + args[i + 2:]))
        return res