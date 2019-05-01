from collections import defaultdict


class Graph:
    graph: dict
    graph_no_weight: dict
    graph_edges_weights: dict
    vertices: int
    graph_as_list: list
    graph_as_dict: dict
    sources: list

    def __init__(self, vert):
        self.graph = defaultdict(list)
        self.vertices = vert
        self.graph_as_list = []
        self.graph_no_weight = defaultdict(list)
        self.graph_edges_weights = defaultdict(list)
        self.graph_as_dict = defaultdict(dict)
        self.sources = list()
