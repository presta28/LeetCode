# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def length(node:optional[TreeNode]):
            if node==None:
                return 0
            left_dept=length(node.left)
            right_dept=length(node.right)
            node_dept=1+max(left_dept,right_dept)
            return node_dept
        return length(root)