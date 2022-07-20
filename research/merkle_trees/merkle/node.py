#!/usr/bin/env python3

from __future__ import annotations

from .util import *


@dataclass(order=True, frozen=True)
class NodeReference:
    max_ordinal: NonnegativeInt
    level: NonnegativeInt

    def min_ordinal(self) -> NonnegativeInt:
        """Get minimum ordinal value.

        This method considers any tree that has a root referenced self.
        The method returns the minimum of the set of max_ordinal values collected from the references of 
        the nodes of such a tree.

        Note: Only returns 0 if self.max_ordinal < (1 << self.level).

        Precondition: self is a valid node reference
        """

        assert(classify_node_reference(self) != NodeReferenceClassification.INVALID)

        num_leaf_nodes_in_complete_tree: PositiveInt = (1 << self.level)

        return self.max_ordinal - (self.max_ordinal % num_leaf_nodes_in_complete_tree)

    def left_child(self) -> Optional[NodeReference]:
        """Get left child node reference.

        A node referenced by self is allowed to have either zero or two children.

        Assuming a node has two children, the first child of such a node is considered the left child.

        This method considers any node with two children that is referenced by self and returns the unique
        reference to the left child of any such node.

        Returns:
            None if self.level == 0.
            Otherwise, returns valid NodeReference to the left child.

        Precondition: self is a valid node reference
        """

        assert(classify_node_reference(self) != NodeReferenceClassification.INVALID)

        if self.level == 0:
            return None

        # Since self.level > 0: self.right_child() != None
        right_child_ref: NodeReference = cast(
            NodeReference, self.right_child())

        # right_child_ref.min_ordinal() cannot be 0 since right_child_ref is a reference to a node that is a right child.

        left_child_max_ordinal: NonnegativeInt = right_child_ref.min_ordinal() - 1
        left_child_level: NonnegativeInt = self.level - 1

        return NodeReference(max_ordinal=left_child_max_ordinal, level=left_child_level)

    def right_child(self) -> Optional[NodeReference]:
        """Get right child node reference.

        A node referenced by self is allowed to have either zero or two children.

        Assuming a node has zero children, the second child of such a node is considered the right child.

        This method considers any node with two children that is referenced by self and returns the unique
        reference to the right child of any such node.

        Returns:
            None if self.level == 0.
            Otherwise, returns valid NodeReference to the right child.

        Precondition: self is a valid node reference
        """

        assert(classify_node_reference(self) != NodeReferenceClassification.INVALID)

        if self.level == 0:
            return None
        elif self.level == 1:
            return NodeReference(max_ordinal=self.max_ordinal, level=(self.level - 1))

        right_child_level: NonnegativeInt = self.level - 1

        p: PositiveInt = (1 << (self.level - 2))
        while p > 0:
            if (self.max_ordinal & p) == 0:
                p >>= 1
                right_child_level -= 1
                assert(right_child_level >= 0)
            else:
                break

        return NodeReference(max_ordinal=self.max_ordinal, level=right_child_level)

    def parent(self, tree_context: NodeReference) -> Optional[NodeReference]:
        """Get parent node reference.

        A node referenced by self can be the child of nodes with many possible distinct references.
        To reduce the possible choices down to exactly one, a disambiguating tree context is required.

        This method considers any tree that has a root referenced by tree_context and which contains a node
        referenced by self. The method returns the unique reference to the node (assuming it exists) within
        any such tree which is the parent of the node referenced by self.

        Parameters:
            tree_context (NodeReference): Reference to the root of a tree that acts as the disambiguating context.

        Returns:
            None if self == tree_context.
            Otherwise, returns valid NodeReference to the parent.

        Precondition: self is a valid reference to a node within the tree referenced by tree_context
        """

        assert(tree_contains_node(tree_context, self))

        if self == tree_context:
            return None

        if (classify_node_reference(self) == NodeReferenceClassification.STABLE) and (self.max_ordinal < tree_context.max_ordinal):
            # self references a node that is a left child of the parent node

            parent_max_ordinal: NonnegativeInt = min(tree_context.max_ordinal, self.max_ordinal + (1 << self.level))

            return NodeReference(max_ordinal=parent_max_ordinal, level=(self.level + 1))

        # self references a node that is a right child of the parent node

        assert(self.max_ordinal > 0)

        parent_level: PositiveInt = self.level + 1

        n: NonnegativeInt = (self.max_ordinal >> self.level)
        p: PositiveInt = 1
        while p <= self.max_ordinal:
            if (n & p) == 0:
                p <<= 1
                parent_level += 1
            else:
                break

        return NodeReference(max_ordinal=self.max_ordinal, level=parent_level)

    def sibling(self, tree_context: NodeReference) -> Optional[NodeReference]:
        """Get sibling node reference.

        A node is allowed to have either zero or two children.

        Assuming a node has two children, the first child of such a node is considered the left child and the second
        child is considered the right child.

        The left child of a node is considered the sibling of the right child of that same node.
        The right child of a node is considered the sibling of the left child of that same node.

        If a node with some specified reference is a right child within the context of a some tree, then its sibling
        has a unique reference regardless of the exact contextual tree chosen.

        However, if a node with some specified reference is a left child within the context of some tree, then its
        sibling can have many possible distinct references depending on the particular contextual tree chosen.

        To reduce the possible choices down to exactly one, a disambiguating tree context is required.

        This method considers any tree that has a root referenced by tree_context and which contains a node
        referenced by self. The method returns a unique reference to the node (assuming it exists) within any such
        tree which is the sibling of the node referenced by self.

        Parameters:
            tree_context (NodeReference): Reference to the root of a tree that acts as the disambiguating context.

        Returns:
            None if self == tree_context.
            Otherwise, returns valid NodeReference to the sibling.

        Precondition: self is a valid reference to a node within the tree referenced by tree_context
        """

        assert(tree_contains_node(tree_context, self))

        if self == tree_context:
            return None

        # Since self != tree_context: self.parent(tree_context) != None
        parent_ref: NodeReference = cast(NodeReference, self.parent(tree_context))

        if self.max_ordinal == parent_ref.max_ordinal:
            # self is reference to a right child of node referenced by parent_ref
            return parent_ref.left_child()
        else:
            # self is reference to a left child of node referenced by parent_ref
            return parent_ref.right_child()


def mutual_parent_of_siblings(sibling1: NodeReference, sibling2: NodeReference) -> Optional[NodeReference]:
    """Get reference to mutual parent of siblings.

    Parameters:
        sibling1 (NodeReference): Reference to a node that is a sibling (within some tree) to another node with reference sibling2.
        sibling2 (NodeReference): Reference to a node that is a sibling (within some tree) to another node with reference sibling1. 

    Returns:
        None if sibling1 and sibling2 are not references to sibling nodes.
        Otherwise, returns valid NodeReference to the mutual parent of the siblings.

    Precondition: sibling1 is a valid node reference
    Precondition: sibling2 is a valid node reference
    """

    assert(classify_node_reference(sibling1) != NodeReferenceClassification.INVALID)
    assert(classify_node_reference(sibling2) != NodeReferenceClassification.INVALID)

    # If they are siblings, find which must necessarily be the left child and which must necessarily be the right child.
    if sibling1.max_ordinal < sibling2.max_ordinal:
        left_child = sibling1
        right_child = sibling2
    elif sibling2.max_ordinal < sibling1.max_ordinal:
        left_child = sibling2
        right_child = sibling1
    else:  # sibling1.max_ordinal == sibling2.max_ordinal
        # Cannot be siblings
        return None

    if left_child.level < right_child.level:
        # Cannot be siblings
        return None

    if (left_child.max_ordinal + (1 << left_child.level)) < right_child.max_ordinal:
        # Cannot be siblings
        return None

    max_parent_level: NonnegativeInt = log2(right_child.max_ordinal + 1).ceil

    assert(left_child.level < max_parent_level)

    parent = right_child.parent(NodeReference(max_ordinal=right_child.max_ordinal, level=max_parent_level))

    assert(parent != None)

    if (left_child.level + 1) != parent.level:
        # Cannot be siblings
        return None

    return parent


class NodeReferenceClassification(Enum):
    # No node can ever be referenced by an INVALID reference.
    INVALID = 1
    # A node referenced by an UNSTABLE reference belongs to a tree with a root that has a unique reference satisfying the
    # constraint that the max_ordinal of that unique root reference is equal to the max_ordinal of the UNSTABLE reference.
    # Within that tree, the node referenced by the UNSTABLE reference must either be a root of the tree or a right child.
    UNSTABLE = 2
    # A node referenced by a STABLE reference exists in all trees with a root that has a reference satisfying the constraint
    # that the max_ordinal of the root reference is greater than or equal to the max_ordinal of the STABLE reference.
    # Within trees with a root reference that has a max_ordinal equal to the max_ordinal of the STABLE reference, the node
    # referenced by the STABLE reference must either be a root of the tree or a right child.
    # Within trees with a root reference that has a max_ordinal strictly greater than the max_ordinal of the STABLE
    # reference, the node referenced by the STABLE reference must be a left child.
    STABLE = 3
    # A node referenced by a RIGHT_STABLE reference exists in all trees with a root that has a reference satisfying the
    # constraint that the max_ordinal of the root reference is greater than or equal to the max_ordinal of the RIGHT_STABLE
    # reference.
    # Within any trees in which the node referenced by a RIGHT_STABLE reference exists, the node referenced by the
    # RIGHT_STABLE reference must either be a root of the tree or a right child.
    RIGHT_STABLE = 4


def classify_node_reference(node_ref: NodeReference) -> NodeReferenceClassification:
    if node_ref.max_ordinal < 0:
        return NodeReferenceClassification.INVALID
    if node_ref.level < 0:
        return NodeReferenceClassification.INVALID

    n: PositiveInt = node_ref.max_ordinal + 1
    p: PositiveInt = (1 << node_ref.level)
    mask: NonnegativeInt = p - 1

    if (n & mask) == 0:
        # Not only is node_ref valid, but it also refers to a stable node.
        if (n & p) == 0:
            return NodeReferenceClassification.RIGHT_STABLE
        else:
            return NodeReferenceClassification.STABLE

    # At this point, node_ref might still be a valid reference but it definitely is not a reference to a stable node.

    allow_level_bitmap: PositiveInt = (node_ref.max_ordinal << 1) + 1
    # The bit at position node_ref.level indicates whether node_ref is valid (if the bit is 1) or not (if the bit is 0).

    if (allow_level_bitmap & p) == 0:
        return NodeReferenceClassification.INVALID

    return NodeReferenceClassification.UNSTABLE


def tree_contains_node(tree_root_ref: NodeReference, node_ref: NodeReference) -> bool:
    """Determines whether referenced node exists can exist in tree with given root reference.

    Precondition: tree_root_ref is a valid node reference
    """

    assert(classify_node_reference(tree_root_ref) != NodeReferenceClassification.INVALID)

    classification = classify_node_reference(node_ref)

    if classification == NodeReferenceClassification.INVALID:
        return False

    if tree_root_ref.max_ordinal < node_ref.max_ordinal:
        return False

    if tree_root_ref.max_ordinal == node_ref.max_ordinal:
        return True

    if classification == NodeReferenceClassification.UNSTABLE:
        return False

    return True


@dataclass
class NodeReferenceRange:
    start: NodeReference
    end: NodeReference


def roots_containing_node(target_node_ref: NodeReference) -> NodeReferenceRange:
    """Get range of references to roots of trees that must hold onto target node with specified reference.

    There are trees with an infinite number of distinct root references that will contain the target node.
    However, there are a finite number of distinct references to the roots of trees which contain the target node in
    a manner that satisfies the following constraints:
       * if the target node is RIGHT_STABLE node, then the tree containing the target node must have a reference
         for its root node that minimizes the max_ordinal; 
       * and, if the target node is not a RIGHT_STABLE node, then there should not exist a sub-tree satisfying all
         of the following properties:
            + the target node is contained in the sub-tree but not at its root;
            + and, the sub-tree is complete.

    In fact, this finite number of distinct references happens to be organized as a contiguous range of references
    where contiguity between two valid NodeReferences is defined as one having a max_ordinal value equal to the
    other's max_ordinal value plus one.

    This function returns that contiguous range of NodeReferences (via a NodeReferenceRange) which describes all 
    the roots of trees that contain the target node in a manner that satisfies the constraints above.

    Parameters:
        target_node_ref (NodeReference): Reference to target node

    Precondition: target_node_ref is a valid reference to a node
    """

    classification = classify_node_reference(target_node_ref)

    assert(classification != NodeReferenceClassification.INVALID)

    start_level: NonnegativeInt = log2(target_node_ref.max_ordinal + 1).ceil

    start = NodeReference(
        max_ordinal=target_node_ref.max_ordinal, level=start_level)

    if classification == NodeReferenceClassification.STABLE:
        end_max_ordinal: NonnegativeInt = target_node_ref.max_ordinal + (1 << target_node_ref.level) - 1
        end_level: NonnegativeInt = log2(end_max_ordinal + 1).ceil
        assert(start.max_ordinal <= end_max_ordinal)
        assert(start.level <= end_level)
        end = NodeReference(max_ordinal=end_max_ordinal, level=end_level)
    else:
        end = NodeReference(max_ordinal=start.max_ordinal, level=start.level)

    return NodeReferenceRange(start=start, end=end)
