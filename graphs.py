#1. BFS
graph = {
    1 : [2,3,4],
    2 : [1,3],
    3 : [2,1],
    4 : [1],
}
v = []
q = []
def bfs(v,q,x):
    v.append(x)
    q.append(x)
    while q:
        s = q.pop(0)
        print(s, end=' ')
        for i in graph[s]:
            if i not in v:
                v.append(i)
                q.append(i)
print("BFS of graph:")
bfs(v,q,3)

#2. DFS
graph = {
    1 : [2,3,4],
    2 : [1,3],
    3 : [2,1],
    4 : [1],
}
v = []
def dfs(v,x):
    v.append(x)
    for i in graph[x]:
        if i not in v:
            dfs(v,i)
    print(v)
print("\nDFS of graph:")
dfs(v,3)

#3. count num of nodes using BFS:
from collections import deque
adj = [[] for i in range(1001)]
def addEdge(v, w):
    adj[v].append(w)
    adj[w].append(v)
def BFS(s, l):
    V = 100
    visited = [False] * V
    level = [0] * V
    for i in range(V):
        visited[i] = False
        level[i] = 0
    queue = deque()
    visited[s] = True
    queue.append(s)
    level[s] = 0
    while (len(queue) > 0):
        s = queue.popleft()
        for i in adj[s]:
            if (not visited[i]):
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
  
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1
    return count
addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(2, 4)
addEdge(2, 5)

level = 2
print("The number of nodes:", BFS(0,level))

#4. count num of trees:
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
def DFS(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFS(adj[u][i], adj, visited)
def countTrees(adj, V):
    visited = [False] * V
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFS(u, adj, visited)
            res += 1
    return res
V = 7
adj = [[] for i in range(V)]
addEdge(adj, 0, 1)
addEdge(adj, 0, 2)
addEdge(adj, 3, 4)
addEdge(adj, 2, 5)
print("\nCount of trees:", countTrees(adj, V))

#5. Detect Cycle:
from collections import defaultdict
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

if g.isCyclic() == 1:
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")

#6. n-Queen's problem
global N
N = 4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
 
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
solveNQ()
 