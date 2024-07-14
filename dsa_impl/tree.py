class TreeNode:
    """
    Node of a binary tree
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def in_order_traversal(root: TreeNode) -> list[int]:
    """
    For binary tree
    1- Travel left subtree
    2- Visit root
    3- Travel right subtree
    """

    def recursive(root: TreeNode):
        traversal_order = []

        def in_order_recursive(node: TreeNode):
            if node:
                if node.left:
                    in_order_recursive(node.left)
                traversal_order.append(node.val)
                if node.right:
                    in_order_recursive(node.right)

        in_order_recursive(root)
        return traversal_order

    def stack(root: TreeNode):
        traversal_order = []
        stack = []
        node = root
        while stack or node is not None:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            traversal_order.append(node.val)
            node = node.right
        return traversal_order

    def morris(root: TreeNode):
        traversal_order = []
        current = root
        while current:
            if current.left is None:
                traversal_order.append(current.val)
                current = current.right
            else:
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = current
                current = current.left
                rightmost.right.left = None
        return traversal_order

    def morris2(root: TreeNode):
        # Recover original tree
        traversal_order = []
        current = root
        while current:
            if current.left is None:
                traversal_order.append(current.val)
                current = current.right
            else:
                rightmost = current.left
                while rightmost.right and rightmost.right != current:
                    rightmost = rightmost.right
                if not rightmost.right:
                    rightmost.right = current
                    current = current.left
                else:
                    rightmost.right = None
                    traversal_order.append(current.val)
                    current = current.right
                # rightmost.right.left = None
        return traversal_order

    return morris2(root)


# Driver code
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(in_order_traversal(root))
