from itertools import chain
from pydoc import visiblename



graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],

]

# 깊이 우선 탐색
# 재귀 함수 사용
# 267페이지 그림 참고
def dfs(g, i, visited): # 그래프주소, index값, 방문한 리스트 주소
    visited[i] = 1 # 방문 처리, 함수 실행하자마자 visited_dfs[0 ~~ ] 첫번째 0이 1 됨.
    print(chr(ord('A') + i), end = ' ') #ord는 ascii코드로 변환해주는 것 > chr(65) 하면 A
    for j in range(len(g)): # g는 그래프의 크기 > 8번 실행
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

# 너비 우선 탐색
# 큐 사용
def bfs(g, i, visited):
    pass

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 0, visited_dfs) # 시작값 i를 뭘로 줘도 똑같이 순회 거쳐서 실행 됨.
print()
bfs(graph, 6, visited_bfs)