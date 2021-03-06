#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-02 23:19:41

# Definition for a binary tree node.
from collections import deque



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Tree(object):
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1


class Solution(object):
    def connect(self, root):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not root:
            return None

        level = [root]
        while level:
            tmp_level = []
            for i in range(len(level)):
                if not level[i]:
                    continue
                tmp_level.append(level[i].left)
                tmp_level.append(level[i].right)
                if i == 0:
                    continue
                level[i-1].next = level[i]
            level = tmp_level

        return root


so = Solution()
a = [-10,-3,0,5,9]
res = so.sortedArrayToBST(a)
print res
