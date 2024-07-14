#!/usr/bin/env python3

from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        def recursive(root):
            # Recursive soltion
            if root:
                if root.left:
                    root.left.next = root.right
                    if root.next:
                        root.right.next = root.next.left
                self.connect(root.left)
                self.connect(root.right)
            return root

        def loop_level(root):
            leftmost = root
            if leftmost:
                while leftmost.left:
                    current = leftmost
                    while current:
                        current.left.next = current.right
                        if current.next:
                            current.right.next = current.next.left
                        current = current.next
                    leftmost = leftmost.left
            return root

        def queue(root):
            # Level order traversal
            if root:
                queue = deque([root])
                rightmost = root
                while queue:
                    current = queue.popleft()
                    if current == rightmost:
                        rightmost = current.right
                    else:
                        current.next = queue[0]
                    if current.left:
                        queue.append(current.left)
                        queue.append(current.right)
            return root
