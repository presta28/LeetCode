# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        count=0
        def leftsum(node:Optinal[TreeNode]):
            nonlocal count
            if node==None:
                return
            if node.left==None:
                return 
            count+=node.left.val
            leftsum(node.left)
            leftsum(node.right)
            return
        leftsum(root)
        return count
        