from common import ListNode


class Solution:
    def insertionSortList(self, head):
        p = head
        while p and p.next:
            pre_sp = sp = head
            while p.next.val > sp.val and sp != p.next:
                pre_sp = sp
                sp = sp.next
            if sp != p.next:
                next_next_node = p.next.next
                if sp == head:
                    p.next.next = head
                    head = p.next
                else:
                    pre_sp.next = p.next
                    p.next.next = sp
                p.next = next_next_node
            else:
                p = p.next

        return head


if __name__ == '__main__':
    solution = Solution()
    from random import shuffle
    l=list(range(200))
    shuffle(l)
    print(l)
    print(solution.insertionSortList(ListNode.list2ListNode(l)))
