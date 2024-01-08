import sys

class Graph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist: list) -> None:
        '''
        Print each distances of vertex from source.
        '''
        for node in range(self.V):
            print(node, '\t', dist[node])
        
    def minDistance(self, dist: list, sptSet: list) -> int:
        '''
        Find the vertiex with minimum distance value
        from vertices set that not yet included in SPT
        '''
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_idx = u
        return min_idx
    
    def dijstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 \
                    and sptSet[y] == False \
                    and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        
        self.printSolution(dist)


if __name__ == "__main__":
    pass