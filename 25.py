from common import ListNode


class Solution:
    def reverseKGroup(self, head, k):
        pre_head, cur_head, p, index = None, head, head, 1
        while p:
            if index % k == 0:
                next_head = p.next
                if pre_head is None:
                    head = p
                else:
                    pre_head.next = p
                pre_head = cur_head
                pre_tmp_p, tmp_p = cur_head, cur_head.next
                while pre_tmp_p != p:
                    next_tmp_p = tmp_p.next
                    tmp_p.next = pre_tmp_p
                    pre_tmp_p, tmp_p = tmp_p, next_tmp_p
                p = cur_head.next = next_head
                cur_head = next_head
            else:
                p = p.next
            index += 1
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseKGroup(ListNode.list2ListNode([1,7,3,2,7,0,1,0,0]),4))
