class Solution:
    def simplifyPath(self, path: str):
        path = path.rstrip('/')[0:]
        dirs = path.split('/')
        stack = []
        for d in dirs:
            if d == '.' or d == '':
                pass
            elif d == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath('/home/'))
    print(solution.simplifyPath('/a/./b/../../c/'))
    print(solution.simplifyPath('/../'))
    print(solution.simplifyPath('/home//foo/'))
