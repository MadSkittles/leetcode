class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre or not post:
            return None
        if len(pre) == len(post) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left_root = pre[1]
        left_pos = post.index(left_root)
        left_len = left_pos + 1
        right_len = len(post) - 1 - left_len
        left_pre, left_post, right_pre, right_post = pre[1 : left_len + 1], post[0:left_len], pre[left_len + 1 :], post[left_len:-1]
        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)
        return root


if __name__ == "__main__":
    solution = Solution()
    print(solution.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]))

