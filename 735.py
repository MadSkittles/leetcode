class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for a in asteroids:
            if not res or not (res[-1] > 0 and a < 0):
                res.append(a)
            else:
                while res and res[-1] > 0 and a < 0:
                    pre_a = res.pop()
                    if pre_a > -a:
                        res.append(pre_a)
                        break
                    elif pre_a < -a:
                        continue
                    else:
                        break
                else:
                    res.append(a)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.asteroidCollision([-2, -1, 1, 2]))
