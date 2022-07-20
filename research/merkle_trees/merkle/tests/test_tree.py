#!/usr/bin/env python3

from lib2to3.pytree import Node
from tkinter.messagebox import NO
import unittest

from ..node import *
from ..tree import *


class TestTraversal(unittest.TestCase):
    def test_traversal_in_tree_over_eleven_leaf_nodes(self):

        root_node_ref: Optional[NodeReference] = None

        def test_reducer(node_ref: NodeReference,
                         sibling_ref: Optional[NodeReference],
                         state: list[tuple[NodeReference, NodeReference]]) \
                -> list[tuple[NodeReference, NodeReference]]:
            nonlocal root_node_ref
            if sibling_ref == None:
                root_node_ref = node_ref
            else:
                state.append((node_ref, sibling_ref))
            return state

        state = traverse_hypothetical_tree(NodeReference(10, 4), NodeReference(5, 0), test_reducer, list())
        self.assertEqual(root_node_ref, NodeReference(10, 4))
        self.assertEqual(len(state), 4)
        self.assertEqual(state[0], (NodeReference(7, 3), NodeReference(10, 2)))
        self.assertEqual(state[1], (NodeReference(7, 2), NodeReference(3, 2)))
        self.assertEqual(state[2], (NodeReference(5, 1), NodeReference(7, 1)))
        self.assertEqual(state[3], (NodeReference(5, 0), NodeReference(4, 0)))


if __name__ == '__main__':
    unittest.main()
