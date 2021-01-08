# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:      
        def serchdepth(node,depth,Max):
            if node == None:
                return Max
            else:
                if Max < depth:
                    Max = depth

                depth += 1
                Max1 = serchdepth(node.left,depth,Max)
                Max2 = serchdepth(node.right,depth,Max)
            if Max1 > Max2:
                return Max1
            else:
                return Max2
                
        depth = 1
        Max = 0
        Max = serchdepth(root,depth,Max)
        print(Max)
        return Max