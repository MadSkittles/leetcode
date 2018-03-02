class Solution:
    def letterCombinations(self, digits):
        button_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        letters_list = []
        for d in digits:
            letters_list.append(button_map[d])

        return self.f(0, letters_list)

    def f(self, index, letters_list):
        if index >= len(letters_list):
            return []
        result = []
        s_list = self.f(index + 1, letters_list) or ['']
        for i in letters_list[index]:
            for s in s_list:
                result.append(i+s)
        return result


if __name__ == '__main__':
    solution=Solution()
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('23'))