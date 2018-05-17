# 给定一个数组和一个目标数，删除最少的数使得数组剩下数的任意子集进行或的结果不等于目标数

def f(nums, n):
    k = 1
    for _ in range(32):
        if not k & n:
            nums = [*filter(lambda x: not x & k, nums)]
        k <<= 1
    min_num, res, k = float('inf'), [], 1
    for _ in range(32):
        if k & n:
            tmp = [*filter(lambda x: x & k, nums)]
            if len(tmp) < min_num:
                min_num = len(tmp)
                res = tmp
        k <<= 1
    return res


if __name__ == '__main__':
    print(f([3, 7, 8, 2, 1, 9, 12], 15))
