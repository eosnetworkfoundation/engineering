#!/usr/bin/env python3

import unittest

from ..node import *


class TestNodeReference(unittest.TestCase):
    def test_with_tree_over_five_leaf_nodes(self):
        self.assertEqual(NodeReference(0, 0).left_child(), None)
        self.assertEqual(NodeReference(0, 0).right_child(), None)
        self.assertEqual(NodeReference(0, 0).parent(NodeReference(1, 1)), NodeReference(1, 1))
        self.assertEqual(NodeReference(1, 0).parent(NodeReference(1, 1)), NodeReference(1, 1))
        self.assertEqual(NodeReference(1, 0).parent(NodeReference(3, 2)), NodeReference(1, 1))
        self.assertEqual(NodeReference(0, 0).sibling(NodeReference(3, 2)), NodeReference(1, 0))
        self.assertEqual(NodeReference(1, 0).sibling(NodeReference(3, 2)), NodeReference(0, 0))
        self.assertEqual(NodeReference(1, 1).left_child(), NodeReference(0, 0))
        self.assertEqual(NodeReference(1, 1).right_child(), NodeReference(1, 0))
        self.assertEqual(NodeReference(4, 3).left_child(), NodeReference(3, 2))
        self.assertEqual(NodeReference(4, 3).right_child(), NodeReference(4, 0))
        self.assertEqual(NodeReference(3, 2).sibling(NodeReference(4, 3)), NodeReference(4, 0))
        self.assertEqual(NodeReference(4, 0).sibling(NodeReference(4, 3)), NodeReference(3, 2))

    def test_with_tree_over_six_leaf_nodes(self):
        self.assertEqual(NodeReference(5, 3).right_child(), NodeReference(5, 1))
        self.assertEqual(NodeReference(5, 1).parent(NodeReference(5, 3)), NodeReference(5, 3))

    def test_with_tree_over_eleven_leaf_nodes(self):
        self.assertEqual(NodeReference(9, 1).left_child(), NodeReference(8, 0))
        self.assertEqual(NodeReference(9, 1).right_child(), NodeReference(9, 0))
        self.assertEqual(NodeReference(10, 2).left_child(), NodeReference(9, 1))
        self.assertEqual(NodeReference(10, 2).right_child(), NodeReference(10, 0))
        self.assertEqual(NodeReference(10, 0).parent(NodeReference(10, 4)), NodeReference(10, 2))
        self.assertEqual(NodeReference(10, 0).sibling(NodeReference(10, 4)), NodeReference(9, 1))
        self.assertEqual(NodeReference(10, 4).left_child(), NodeReference(7, 3))
        self.assertEqual(NodeReference(10, 4).right_child(), NodeReference(10, 2))
        self.assertEqual(NodeReference(10, 2).parent(NodeReference(10, 4)), NodeReference(10, 4))
        self.assertEqual(NodeReference(7, 3).sibling(NodeReference(10, 4)), NodeReference(10, 2))
        self.assertEqual(NodeReference(5, 1).parent(NodeReference(7, 3)), NodeReference(7, 2))


class TestMutualParentOfSiblings(unittest.TestCase):
    def test_with_tree_over_four_leaf_nodes(self):
        self.assertEqual(mutual_parent_of_siblings(NodeReference(1, 1), NodeReference(3, 1)), NodeReference(3, 2))
        self.assertEqual(mutual_parent_of_siblings(NodeReference(1, 1), NodeReference(3, 2)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(3, 1), NodeReference(3, 2)), None)

    def test_with_tree_over_five_leaf_nodes(self):
        self.assertEqual(mutual_parent_of_siblings(NodeReference(3, 1), NodeReference(5, 1)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(3, 2), NodeReference(5, 1)), NodeReference(5, 3))

    def test_with_tree_over_eleven_leaf_nodes(self):
        self.assertEqual(mutual_parent_of_siblings(NodeReference(3, 1), NodeReference(7, 2)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(7, 2), NodeReference(10, 2)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(7, 2), NodeReference(10, 0)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(10, 0), NodeReference(7, 3)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(10, 0), NodeReference(7, 3)), None)
        self.assertEqual(mutual_parent_of_siblings(NodeReference(10, 2), NodeReference(7, 3)), NodeReference(10, 4))
        self.assertEqual(mutual_parent_of_siblings(NodeReference(7, 3), NodeReference(10, 2)), NodeReference(10, 4))

if __name__ == '__main__':
    unittest.main()
