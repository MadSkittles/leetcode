class Solution:
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(0, lo)
        return lo == 0

    def checkValidString1(self, s):
        stack1, stack2, cnt = [], [], 0
        m = {'(': 1, ')': -1, '*': 0}
        for c in s:
            if c == '(' or c == '*':
                stack1.append(c)
            cnt += m[c]
            if cnt < 0:
                while stack1 and stack1[-1] != '*':
                    stack2.append(stack1.pop())
                if not stack1:
                    return False
                stack1.pop()
                cnt += 1
                while stack2:
                    stack1.append(stack2.pop())
            elif c == ')':
                while stack1 and stack1[-1] != '(':
                    stack2.append(stack1.pop())
                stack1.pop()
                while stack2:
                    stack1.append(stack2.pop())
        if cnt > 0:
            cnt1 = 0
            for c in stack1:
                if c == '(':
                    cnt1 += 1
                else:
                    cnt1 = max(cnt1 - 1, 0)
            return cnt1 == 0
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkValidString("()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"))
