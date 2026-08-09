# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node1:Optional):
            if node1==None:
                return
            temp =node1.left
            node1.left=node1.right
            node1.right=temp
            swap(node1.left)
            swap(node1.right)
        swap(root)
        return root
        