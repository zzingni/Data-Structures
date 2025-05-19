
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph =[[0 for _ in range(size)] for _ in range(size)]

G1 = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("# G1 무방향 그래프 #")
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()


G2 = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G2.graph[0][1] = 1; G2.graph[0][2] = 1
G2.graph[3][0] = 1; G2.graph[3][2] = 1

print()

print("# G2 방향 그래프 #")
for row in range(G2.SIZE):
    for col in range(G2.SIZE):
        print(G2.graph[row][col], end=' ')
    print()


G_self = Graph(4)
# 0 == A, 1 == B, 2 == C, 3 == D
G_self.graph[0][3] = 1
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1
G_self.graph[2][1] = 1
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1

print()

print("# G_self 무방향 그래프 #")
for row in range(G_self.SIZE):
    for col in range(G_self.SIZE):
        print(G_self.graph[row][col], end=' ')
    print()
