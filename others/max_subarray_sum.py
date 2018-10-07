def max_subarray_sum(A):
    max_sum, cur_max = 0, float("-inf")
    for a in A:
        cur_max = max(cur_max + a, a)
        max_sum = max(max_sum, cur_max)
    return max_sum


if __name__ == "__main__":
    print(max_subarray_sum([-3, 5, 5]))

