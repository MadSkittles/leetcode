from common import ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pA, pB, lA, lB = headA, headB, 0, 0
        while pA:
            lA += 1
            pA = pA.next
        while pB:
            lB += 1
            pB = pB.next
        pA, pB = headA, headB
        while lA > lB:
            pA = pA.next
            lA -= 1
        while lB > lA:
            pB = pB.next
            lB -= 1
        while pA and pB and pA != pB:
            pA = pA.next
            pB = pB.next
        return pA and pB


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode.list2ListNode([1, 2, 3])
    l2 = ListNode.list2ListNode([1, 2, 3, 4, 5, 6])
    l3 = ListNode.list2ListNode([7])
    l1.append(l3)
    l2.append(l3)
    print(solution.getIntersectionNode(l1, l2))
