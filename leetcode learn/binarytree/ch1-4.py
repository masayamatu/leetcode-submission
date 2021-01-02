# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def leveltraverse(node,ans,depth):
            if node == None:
                return None
            else:
                if len(ans) <= depth:
                    ans += [[node.val]]
                else:
                    ans[depth].append(node.val)
                leveltraverse(node.left,ans,depth+1)
                leveltraverse(node.right,ans,depth+1)
        ans = []
        depth=0
        leveltraverse(root,ans,depth)
        return ans