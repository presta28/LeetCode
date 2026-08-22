# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node:Optional[TreeNode]):
            if node==None:
                return True
            if node.left!=None and node.val<=node.left.val:
                return False
            if node.right!=None and node.val>=node.right.val:
                return False
            left=valid(node.left)
            right=valid(node.right)
            return left and right
        return valid(root)