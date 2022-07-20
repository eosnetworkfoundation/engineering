#!/usr/bin/env python3

from .node import *


def traverse_hypothetical_tree(tree_root_ref: NodeReference,
                               target_node_ref: NodeReference,
                               reducer: Callable[[NodeReference, Optional[NodeReference], Any], Any],
                               initial_state: Any = None) -> Any:
    """Traverse a hypothetical tree with a root referenced by tree_root_ref from that root to the specified target node.

    For each hypothetical node visited along the traversal, reducer is called with the third argument set the current value of the internal state.
    For all nodes other than the root node, reducer is called with a reference to the visited node as well as a reference to its sibling.
    For the root node, reducer is called with a reference to the visited node but the sibling argument is None (since the root has no sibling).

    Parameters:
        tree_root_ref (NodeReference): Reference to root node of the hypothetical tree to traverse
        target_node_ref (NodeReference): Reference to target node
        reducer (function (NodeReference, Optional[NodeReference], Any) -> Any): 
            Function to call for each hypothetical node visited along traversal.
            Function called with reference to node visited, reference to its sibling node, and the current value of the internal state.
            Function is expected to return the next value of the internal state.

    Returns:
        Value of the internal state after visiting all hypothetical nodes in the traversal.

    Precondition: target_node_ref is a valid reference to a node within the hypothetical tree
    """

    assert(tree_contains_node(tree_root_ref, target_node_ref))

    num_bits: PositiveInt = log2(tree_root_ref.max_ordinal).floor + 1

    # Convert target_node_ref.max_ordinal into num_bits long bit sequence
    bit_seq = [Bit(bit) for bit in "{:0{size}b}".format(target_node_ref.max_ordinal, size=num_bits)]

    bit_seq_iter = iter(bit_seq)

    cur_node_ref: NodeReference = tree_root_ref
    internal_state: Any = reducer(cur_node_ref, None, initial_state)

    if cur_node_ref.level <= target_node_ref.level:
        assert(cur_node_ref.level == target_node_ref.level)
        assert(cur_node_ref.max_ordinal == target_node_ref.max_ordinal)
        return internal_state

    maybe_bit: Optional[Bit] = next(bit_seq_iter, None)

    while maybe_bit != None:
        if maybe_bit == 0:
            next_node_ref = cur_node_ref.left_child()
        else:
            next_node_ref = cur_node_ref.right_child()
        assert(next_node_ref != None)

        for i in range(cur_node_ref.level, next_node_ref.level, -1):
            maybe_bit = next(bit_seq_iter, None)

        cur_node_ref = next_node_ref
        sibling_node_ref: NodeReference = cast(NodeReference, next_node_ref.sibling(tree_root_ref))

        internal_state = reducer(cur_node_ref, sibling_node_ref, internal_state)

        if cur_node_ref.level <= target_node_ref.level:
            assert(cur_node_ref.level == target_node_ref.level)
            assert(cur_node_ref.max_ordinal == target_node_ref.max_ordinal)
            break

    return internal_state


@dataclass
class BranchProof:
    root: NodeReference
    target: NodeReference
    witnesses: list[NodeReference]


def generate_branch_proof(tree_root_ref: NodeReference, target_node_ref: NodeReference) -> BranchProof:
    def branch_proof_reducer(node_ref: NodeReference, sibling_ref:
                             Optional[NodeReference], state: list[NodeReference]) -> list[NodeReference]:
        if sibling_ref != None:
            state.append(sibling_ref)
        return state

    state: list[NodeReference] = traverse_hypothetical_tree(
        tree_root_ref, target_node_ref, branch_proof_reducer, list())
    state.reverse()
    return BranchProof(root=tree_root_ref, target=target_node_ref, witnesses=state)


def verify_proof(proof: BranchProof) -> bool:
    cur_node_ref: NodeReference = proof.target
    for witness_ref in proof.witnesses:
        parent_ref = mutual_parent_of_siblings(cur_node_ref, witness_ref)
        if parent_ref == None:
            return False
        # Computed inner node parent_ref
        cur_node_ref = parent_ref
    return cur_node_ref == proof.root


def lookup_nodes(proof: BranchProof) -> dict[NodeReference, list[NodeReference]]:
    """Determine efficient strategy to lookup necessary nodes to generate actual proof.

    Returns:
        Dictionary where the key is a valid NodeReference of the root of tree that should be looked at to grab the nodes
        referenced in list of valid NodeReferences which acts as the value for that key.

        The algorithm guarantees that not only do the NodeReferences in the value list refer to nodes that will be part 
        of the tree whose root is referred to by the key, but that they will be nodes that are efficient to store as
        part of that tree without being wasteful in storing too much data that is unnecessary to advance the Merkle tree
        as new leaf nodes are appended to it.

        A NodeReference will not be duplicated across the lists of different key-value pairs.
        In addition, the union of the NodeReferences contained in all the value lists of the dictionary is exactly the set
        of NodeReferences taken from proof.
    """

    key_value_pairs = list(map(lambda n: (roots_containing_node(n).end, n),
                           [proof.root, proof.target, *proof.witnesses]))
    key_value_pairs.sort(key=lambda p: p[0])

    nodes_to_lookup: dict[NodeReference, list[NodeReference]] = {k: [] for k in map(lambda p: p[0], key_value_pairs)}

    for p in key_value_pairs:
        nodes_to_lookup[p[0]].append(p[1])

    return nodes_to_lookup
