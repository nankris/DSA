# Leetcode solution, one of my favorite recursive problem

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)

        return max(left_d, right_d) +1 
        


