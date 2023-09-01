 class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse_both_trees(p_node, q_node):            
            if p_node is None and q_node is None:
                return True
            if p_node is None or q_node is None:
                return False
            if p_node.val != q_node.val:
                return False
            left = traverse_both_trees(p_node.left, q_node.left)
            right = traverse_both_trees(p_node.right, q_node.right)

            return left and right

        res = traverse_both_trees(p, q)

        if res:
            return True
        else:
            return False



 class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst1 = []
        def traverse(current_node):
            if current_node is None:
                lst1.append("null")
                return
            traverse(current_node.right)
            traverse(current_node.left)
            lst1.append(current_node.val)
        
        lst2 = []
        def traverse2(current_node):
            if current_node is None:
                lst2.append("null")
                return
            traverse2(current_node.right)
            traverse2(current_node.left)
            lst2.append(current_node.val)

        traverse(p)
        traverse2(q)

        if lst1 == lst2:
            return True
        else:
            return False
