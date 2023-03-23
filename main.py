
graph = [
    [11],
    [2],
    [1, 3],
    [2, 4, 6],
    [3, 9],
    [4],
    [3, 7],
    [6, 9],
    [9, 11],
    [7, 4, 8],
    [11], 
    [8, 10, 0]
]


marked = [ False for i in range(12)]

#5

def dfs(v: int):
    print(v)
    marked[v] = True
    for adj in graph[v]:
        isMarked = marked[adj]
        if not isMarked:
            dfs(adj)


# 3 => 2
 
dfs(7)
