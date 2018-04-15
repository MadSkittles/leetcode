from common import ListNode


class Solution:
    def splitListToParts(self, root, k):
        length, node = 0, root
        while node:
            node = node.next
            length += 1
        part_length, add_length_index, index, res, p = length // k, length % k, 0, [], root
        while index < k:
            l = part_length + (index < add_length_index)
            res.append(p)
            while l > 1 and p:
                l -= 1
                p = p.next
            if p:
                p.next, p = None, p.next
            index += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitListToParts(ListNode.list2ListNode([1, 2, 3]), 5))
    print(solution.splitListToParts(ListNode.list2ListNode([]), 3))
