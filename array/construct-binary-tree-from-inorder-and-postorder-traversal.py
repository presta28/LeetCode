# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        postindex = len(postorder) - 1

        def Tree(left, right):
            nonlocal postindex

            if left > right:
                return None

            target = postorder[postindex]

            root_index = -1

            for i in range(left, right + 1):
                if inorder[i] == target:
                    root_index = i
                    break

            postindex -= 1

            root = TreeNode(target)

            # IMPORTANT: right subtree first
            right_tree = Tree(root_index + 1, right)
            left_tree = Tree(left, root_index - 1)

            root.left = left_tree
            root.right = right_tree

            return root

        return Tree(0, len(inorder) - 1)