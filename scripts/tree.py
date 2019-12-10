from services import fasta


def tree(file_name):
    """
    Prints the number of edges to be added to the graph to produce a tree.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Completing a Tree

    An undirected graph is connected if there is a path connecting any two
    nodes. A tree is a connected (undirected) graph containing no cycles; this
    definition forces the tree to have a branching structure organized around
    a central core of nodes, just like its living counterpart.

    We have already grown familiar with trees in “Mendel's First Law”, where we
    introduced the probability tree diagram to visualize the outcomes of a
    random variable.

    In the creation of a phylogeny, taxa are encoded by the tree's leaves, or
    nodes having degree 1. A node of a tree having degree larger than 1 is
    called an internal node.

    Given: A positive integer n (n≤1000) and an adjacency list corresponding
    to a graph on n nodes that contains no cycles.

    Return: The minimum number of edges that can be added to the graph to
    produce a tree.
    """

    data = fasta.get(file_name, remove_new_line=False)
    data = data.split("\n")
    n = int(data[0])
    data = data[1:-1]

    edges = n - 1 - len(data)

    print(edges)
