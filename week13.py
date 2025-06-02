# 깊이우선탐색의 stack 활용
# 나중에 재귀함수 사용해서 코드 짜보기 > 기존 재귀함수 true, false 리턴하는 걸로 바꿔야 함.
# mst

class Graph: # () 없앰
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

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

def find_vertex(g, find_vtx): # 중요, 연결 유무 확인 함수.
    visited_ary = list()
    start = 0 # 시작 도시 index
    dfs(g, start, visited_ary)
    return find_vtx in visited_ary # True or False

def dfs(g, current, visited):
    visited.append(current) # 현재 노드를 넣고 시작 (인천부터 시작)
    for vertex in range(graph_size):
        if g.graph[current][vertex] > 0 and vertex not in visited: # 가중치 값이 있으면서 방문하지 않았을 때
            dfs(g, vertex, visited)

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
	for k in range(graph_size) :
		if g1.graph[i][k] != 0 :
			edge_ary.append([g1.graph[i][k], i, k])
print(edge_ary)

edge_ary.sort(reverse=True)
print(edge_ary)

new_ary = list()
for i in range(1, len(edge_ary), 2): # 무방향 그래프 사이즈 줄임 > 2개씩 차이
	new_ary.append(edge_ary[i])
print(new_ary)

index = 0
while len(new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복 > 사이클 만들어지면 안 되니까 노드 개수 -1 >> 최소신장트리
	# [가중치, 출발도시, 도착도시]
	# 백업 > 간선 끊어지면 안 되니까.
	start = new_ary[index][1] # 출발도시
	end = new_ary[index][2] # 도착도시
	save_cost = new_ary[index][0] # 가중치

	# 출발도시, 도착도시 0, 0으로 바꾸기
	g1.graph[start][end] = 0
	g1.graph[end][start] = 0

	# 지운 출발도시, 도착도시 있는지 찾기
	# 연결되어 있으면 true, 아니면 false
	start_reachable = find_vertex(g1, start)
	end_reachable = find_vertex(g1, end)  # 광주-부산 지우면 false 옴.

	if start_reachable and end_reachable :
		del new_ary[index] # 둘 다 true면 해당 간선 삭제

	# 도시 간선 끊기면 백업
	else:
		g1.graph[start][end] = save_cost
		g1.graph[end][start] = save_cost
		index = index + 1 # 인덱스 증가, 증가 안 하면 무한루프. 노드 -1까지만 돌아야 함.

print('최소 비용 계산')
print_graph(g1)

total_cost = 0
for i in range(graph_size):
	for j in range(graph_size):
		if g1.graph[i][j] != 0:
			total_cost = total_cost + g1.graph[i][k]

total_cost = total_cost // 2  # 무방향 그래프니까 // 2 > 절반 날려야 함.
print(f"최소 비용 계산 :  {total_cost}")