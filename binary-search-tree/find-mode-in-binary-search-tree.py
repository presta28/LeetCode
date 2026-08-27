# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictt={}
        listt=[]
        def find(node:Optinal[TreeNOde]):
            nonlocal dictt
            if node==None:
                return
            find(node.left)
            if node.val not in dictt:
                dictt[node.val]=1
            else:
                dictt[node.val]+=1
            find(node.right)
            return
        find(root)
        max_freq=0
        for key, value in dictt.items():
            if value > max_freq:
                listt = [key]
                max_freq = value

            elif value == max_freq:
                listt.append(key)
        return listt
