from common import ListNode


class Solution:
    def deleteDuplicates(self, head):
        pre_p = p = head
        while p:
            cur_val, cur_p = p.val, p
            while p.next and p.next.val == cur_val:
                p = p.next
            if cur_p != p:
                if head == cur_p:
                    head = p.next
                    pre_p = head
                else:
                    pre_p.next = p.next
            else:
                pre_p = p
            p = p.next

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.deleteDuplicates(ListNode.list2ListNode([1, 2, 3, 3, 4, 4, 5])))
    print(solution.deleteDuplicates(ListNode.list2ListNode([1, 1, 2, 2])))
    print(solution.deleteDuplicates(ListNode.list2ListNode([1, 1, 1, 2, 3])))
    print(solution.deleteDuplicates(ListNode.list2ListNode([1, 2, 3, 3, 4, 4, 5, 6, 6])))
