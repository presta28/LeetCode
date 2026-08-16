# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        count=0
        def tilt(node:Optional[TreeNode]):
            nonlocal count
            if node==None:
                return 0 
            left=tilt(node.left)
            right=tilt(node.right)
            count+=abs(left-right)
            return left+right+node.val
        tilt(root)
        return count
        