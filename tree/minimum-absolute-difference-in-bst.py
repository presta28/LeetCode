# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff=float('inf')
        def getmin(node:Optional[TreeNode],upper:int):
            nonlocal min_diff 
            if node==None:
                return 
            getmin(node.left,node.val)
            first = node.val
            diff = abs(first-upper)
            if diff <min_diff:
                min_diff = diff
            getmin(node.right,node.val)
            return 
        getmin(root,0)
        return min_diff

        