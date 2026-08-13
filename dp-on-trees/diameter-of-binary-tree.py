# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode],) -> int:
        largest_length=0
        def diameter(node:Optional[TreeNode]):
            nonlocal largest_length
            if node==None:
                return 0 
            left_height=diameter(node.left)
            right_height=diameter(node.right)
            if left_height>right_height:
                height=left_height+1
            else:
                height=right_height+1
            length = left_height+right_height
            if length>largest_length:
                largest_length=length
            return height
        diameter(root)
        return largest_length