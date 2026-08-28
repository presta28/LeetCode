# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def range_sum(node):
            if node == None:
                return 0

            if node.val < low:
                return range_sum(node.right)

            if node.val > high:
                return range_sum(node.left)

            return node.val + range_sum(node.left) + range_sum(node.right)

        return range_sum(root)             