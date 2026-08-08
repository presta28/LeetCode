# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def postorder(node:optional[TreeNode]):
            if node==None:
                return
            postorder(node.left)
            postorder(node.right)
            list1.append(node.val)
        postorder(root)
        return list1
        