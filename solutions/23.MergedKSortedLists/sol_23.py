#!/usr/bin/env python3 

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      value_tree_node_table = {}
      
      # Initialize binary tree
      node = next(iter(lists))
      min_node = TreeNode(val=node.val)
      max_node = min_node
      node = node.next
      for node in lists:
        while node:
          if node.val >= max_node.val:
            max_node.right = TreeNode(val=node.val)
            max_node = max_node.right
          elif min_node.val < node.val < max_node.val:
             
          
          node = node.next
          
      
        )(((((()())()()))()(()))(