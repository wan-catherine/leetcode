# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_before(self, root):
        if root == None:
            return []
        self.helper(root)

    def helper(self, node):
        if node == None or node.left == None or node.right == None:
            return

        node.left.next = node.right
        # print(str(node.left.val) + " --> " + str(node.right.val))
        if node.next != None and node.next.left != None:
            node.right.next = node.next.left
            # print(str(node.right.val) + " --> " + str(node.next.left.val))
        self.helper(node.left)
        self.helper(node.right)

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        parent = root
        while parent:
            if not parent.left:
                break
            cur = parent.left
            cur.next = parent.right
            cur = cur.next
            node = parent.next
            while node:
                cur.next = node.left
                cur = cur.next
                cur.next = node.right
                cur = cur.next
                node = node.next
            parent = parent.left
        return root