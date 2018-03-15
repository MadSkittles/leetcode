class Solution:
    def lengthLongestPath(self, input: str):
        files = input.split("\n")
        num_of_tab = 0
        stack = ['']
        res = 0
        for f in files:
            i = 0
            while f.startswith(i * '\t'):
                i += 1
            while num_of_tab > i:
                stack.pop()
                num_of_tab -= 1
            if '.' not in f:
                stack.append(stack[-1] + ('/' if stack[-1] else '') + f.lstrip('\t'))
                num_of_tab = i + 1
            else:
                res = max(res, len(stack[-1] + ('/' if stack[-1] else '') + f.lstrip('\t')))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthLongestPath('a'))
    print(solution.lengthLongestPath("skd\n\talskjv\n\t\tlskjf\n\t\t\tklsj.slkj\n\t\tsdlfkj.sdlkjf\n\t\tslkdjf.sdfkj\n\tsldkjf\n\t\tlskdjf\n\t\t\tslkdjf.sldkjf\n\t\t\tslkjf\n\t\t\tsfdklj\n\t\t\tlskjdflk.sdkflj\n\t\t\tsdlkjfl\n\t\t\t\tlskdjf\n\t\t\t\t\tlskdjf.sdlkfj\n\t\t\t\t\tlsdkjf\n\t\t\t\t\t\tsldkfjl.sdlfkj\n\t\t\t\tsldfjlkjd\n\t\t\tsdlfjlk\n\t\t\tlsdkjf\n\t\tlsdkjfl\n\tskdjfl\n\t\tsladkfjlj\n\t\tlskjdflkjsdlfjsldjfljslkjlkjslkjslfjlskjgldfjlkfdjbljdbkjdlkjkasljfklasjdfkljaklwejrkljewkljfslkjflksjfvsafjlgjfljgklsdf.a"))
