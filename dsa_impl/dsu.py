class Dsu:
    def __init__(self) -> None:
        self.parents = []
        self.ranks = []

    def make_set(self, v: int):
        self.parent[v] = v
        self.rank[v] = 0

    def find_set(self, v: int) -> int:
        if v == self.parents[v]:
            return v
        self.parents[v] = self.find_set(
            self.parents[v]
        )  # Path compression optimization
        return self.parents[v]

    def union_set(self, a: int, b: int):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.ranks[a] < self.ranks[b]:  # Union by rank
                a, b = b, a
            self.parents[b] = a
            if self.ranks[a] == self.ranks[b]:
                self.ranks[a] += 1
