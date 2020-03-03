import random
import pdb

legal_moves=[(2,-1), (2,1), (1, 2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (-1, -2)]

m, n = 10, 10

A=[[random.randint(0,1) for i in range(m)] for i in range(n)]

class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, src, dst):
        if src in self.graph:
            tmp = self.graph[src]
            self.graph[src] = tmp + [dst]
        else:
            self.graph[src] = [dst]
    def show(self):
        print self.graph

    def get_vertexes_without_connection(self):
        vertexes_without_conn = list()
        for key in self.graph:
            vertexes_without_conn = vertexes_without_conn + self.graph[key]
        return vertexes_without_conn

    def dfs(self,graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extended(graph[vertex] - visited)
        return visited

def turn(graph, current_position, board, m, n):
    for move in legal_moves:
        new_pos = (current_position[0] + move[0], current_position[1] + move[1])
        if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] <= (m-1) and new_pos[1] <= (n-1) and board[new_pos[0]][new_pos[1]] == 0:
            graph.add_edge(current_position, new_pos)
    return graph
for row in A:
    print row
#pdb.set_trace()
g = Graph()

res = turn(g, (0,0), A, m, n)
g.show()

for vertex in g.get_vertexes_without_connection():
    turn(g, vertex, A, m, n)

g.show()

for vertex in g.get_vertexes_without_connection():
    turn(g, vertex, A, m, n)

g.show()


for vertex in g.get_vertexes_without_connection():
    turn(g, vertex, A, m, n)

g.show()

for vertex in g.get_vertexes_without_connection():
    turn(g, vertex, A, m, n)

g.show()
