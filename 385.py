from common import NestedInteger


class Solution:
    def deserialize(self, s):
        stack, n = [], ''
        for c in s + '#':
            if c == '[':
                stack.append(NestedInteger())
            elif c in '-1234567890':
                n += c
            elif c == ',':
                if n:
                    if len(stack):
                        stack[-1].add(NestedInteger(int(n)))
                    n = ''
            elif c == ']':
                if n:
                    if len(stack):
                        stack[-1].add(NestedInteger(int(n)))
                    n = ''
                nestedList = stack.pop()
                if len(stack):
                    stack[-1].add(nestedList)
                else:
                    stack.append(nestedList)
            else:
                if n:
                    if len(stack):
                        stack[-1].add(NestedInteger(int(n)))
                    else:
                        stack.append(NestedInteger(int(n)))
                    n = ''
        return stack[0]
