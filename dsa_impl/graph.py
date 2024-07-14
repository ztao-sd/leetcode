import inspect
from enum import Enum
from collections import defaultdict, deque
from collections.abc import Hashable


class GraphRepresentationType:
    ADJACENCY_LIST = "ADJACENCY_LIST"
    ADJACENCY_MATRIX = "ADJACENCY_MATRIX"


class Graph:
    """
    Implement a graph based on adjacency list (sequential representation)
    Space complecity O(V+E)
    Adding a vertex O(1)
    Adding an edge O(1)
    Removing a vertex O(V+E)
    Removing an edge O(E)
    Querying an edge O(V)
    """

    def __init__(
        self, repr: GraphRepresentationType = GraphRepresentationType.ADJACENCY_LIST
    ) -> None:
        self.adj_list = defaultdict(list)
        self._repr = repr

    def add_vertex(self, v: Hashable):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def remove_vertex(self, v: Hashable):
        if v in self.adj_list:
            self.adj_list.pop(v)
        for _list in self.adj_list.values():
            for _v in _list:
                if v == _v:
                    _list.remove(_v)

    def add_edge(self, v1: Hashable, v2: Hashable):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1: Hashable, v2: Hashable):
        if v1 in self.adj_list[v2]:
            self.adj_list[v2].remove(v1)
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove[v2]

    def breath_first_search(self, start: Hashable) -> list[Hashable]:
        visited = set()
        traversal_order = []
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbour in self.adj_list[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return traversal_order

    def depth_first_search(self, start: Hashable) -> list[Hashable]:
        visited = set()
        traversal_order = []
        stack = deque([start])
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbour in self.adj_list[vertex]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return traversal_order

    def depth_first_search2(self, start: Hashable) -> list[Hashable]:
        visited = set()
        traversal_order = []

        def dfs(vertex: Hashable):
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbour in self.adj_list[vertex]:
                    if neighbour not in visited:
                        dfs(neighbour)

        dfs(start)
        return traversal_order


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")

    print(graph.breath_first_search("A"))
    print(graph.depth_first_search("A"))
    print(graph.depth_first_search2("A"))

# end main
