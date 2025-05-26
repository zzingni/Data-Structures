from collections import deque

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

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end = ' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(g, i, visited):
    queue = deque([i]) # popleft, append (deque를 queue처럼 사용)
    visited[i] = True
    while queue: # queue안에 값이 존재할 동안
        i = queue.popleft() # popleft 하면 dequeue랑 동일
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True

visited_dfs = [0 for _ in range(len(graph))]
# visited_bfs = [0 for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))] # 위에 문장과 동일. 비교할 때 False로 비교해야 함.
dfs(graph, 0, visited_dfs)
print()
bfs(graph, 1, visited_bfs)