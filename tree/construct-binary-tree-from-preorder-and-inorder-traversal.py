# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(0)
        def Tree(array:List[int]):
            nonlocal preorder
            target= preorder[0]
            if len(array)==0:
                return None
            count=0
            for i in range(len(array)):
                if array[i]==target:
                    break
                count+=1
            preorder.pop(0)
            if len(array)==1:
                return TreeNode(array[0])
            root = TreeNode(array[count])
            left_tree = Tree(array[:count])
            right_tree = Tree(array[count+1:])
            root.left=left_tree
            root.right=right_tree
            return root
        return Tree(inorder)



        