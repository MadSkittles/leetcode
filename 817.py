from common import ListNode


class Solution:
    def numComponents(self, head, G):
        hsh = {}
        for idx, val in enumerate(G):
            hsh[val] = idx
        id = 0
        while head:
            if head.val in hsh:
                hsh[head.val] = id
            else:
                id += 1
            head = head.next
        return len(set(hsh.values()))


if __name__ == '__main__':
    solution = Solution()
    print(solution.numComponents(ListNode.list2ListNode([1, 2, 0, 4, 3]), [3, 4, 0, 2, 1]))
