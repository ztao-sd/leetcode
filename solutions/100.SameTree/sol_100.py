#!/usr/bin/env python3

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def recursive(p, q):

            def pre_order_recursive(p, q):
                if p and q:
                    if p.val != q.val:
                        return False
                    return pre_order_recursive(p.left, q.left) and pre_order_recursive(
                        p.right, q.right
                    )
                elif (not p) == q:
                    return False
                return True

        return recursive(p, q)
