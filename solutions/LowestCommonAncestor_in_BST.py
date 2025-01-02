class TreeNode:
    """Define class for TreeNode"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree.

    The Lowest Common Ancestor between two nodes p and q is the lowest node in the tree T 
    such that both p and q are descendants of the node. The ancestor is allowed to be a 
    descendant of itself.

    Args:
        root (TreeNode): The root of the Binary Search Tree.
        p (TreeNode): The first node in the BST.
        q (TreeNode): The second node in the BST to find LCA with.

    Returns:
        TreeNode: The Lowest Common Ancestor of nodes p and q.

    Examples:
        Given the Binary Search Tree Structure:
                 5
               /   \
              3     8
             / \   / \
            1   4 7   9
             \
              2

        Example 1:
        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
        Output: 5
        
        Example 2:
        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
        Output: 3
    """
    start = root
