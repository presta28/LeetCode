# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node:Optional[TreeNode],lower,upper):
            if node==None:
                return True
            if node.val>=upper or node.val<=lower:
                return False
            left = valid(node.left, lower, node.val)
            right = valid(node.right, node.val, upper)

            return left and right

        return valid(root, float("-inf"), float("inf"))
