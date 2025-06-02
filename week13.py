# 크루스칼 알고리즘
# DisjoinSet 클래스 생성

class Graph: # () 없앰
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

class DisjointSet: # 크루스칼 알고리즘을 위한 유틸리티 클래스
	def __init__(self, n):
		self.parent = [i for i in range(n)]
	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root != y_root:
			self.parent[y_root] = x_root
			return True
		return False # False 대문자 주의

def print_graph(g): # 스네이크 표기법
    print(' ', end = ' ')
    for v in range(len(g.graph)) :
        print(name_ary[v], end =' ')
    print()
    for row in range(len(g.graph)) :
        print(name_ary[row], end =' ')
        for col in range(len(g.graph)) : # g객체의 graph 속성의 길이
            print(f"{g.graph[row][col]:2d}", end=' ')
        print()
    print()

g1 = None
name_ary = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edge_ary = []  # 결과적으로 2d list
for i in range(graph_size) :
	for j in range(graph_size) :
		if g1.graph[i][j] != 0 :
			edge_ary.append([g1.graph[i][j], i, j])
print(edge_ary)

edge_ary.sort() # 오름차순. 가중치가 작은 것들부터 정렬. 이 파트 중요!!!!!! 시험 나올듯..?
print(edge_ary)

new_ary = list()
for i in range(1, len(edge_ary), 2): # 무방향 그래프 사이즈 줄임 > 2개씩 차이
	new_ary.append(edge_ary[i])
print(new_ary)


ds = DisjointSet(graph_size)

# 크루스칼 오름차순은 range(1, 길이, 2) 코드로 건너띄어서 저장하는 코드도 필요없음.
mst_edges = list()
mst_cost = 0

for cost, s, e in edge_ary: # 비용, 시작도시, 끝도시
	if ds.union(s, e):
		mst_edges.append((cost, s, e))
		mst_cost = mst_cost + cost

# 새로운 트리 만들기 (최소신장트리)
mst_graph = Graph(graph_size)
for cost, s, e in mst_edges:
	mst_graph.graph[s][e] = cost
	mst_graph.graph[e][s] = cost # 무방향 그래프라 반대 방향으로도.

print('최소 비용 계산')
print_graph(mst_graph)

print(f"최소 비용 계산 :  {mst_cost}")