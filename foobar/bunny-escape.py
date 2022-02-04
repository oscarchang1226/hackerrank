def solution(m):
    maxH = len(m)
    maxW = len(m[0])
    minPath = 2 ** 32 - 1
    for i in getAllMaps(m):
        pathLength = boardWithPathLength(0, 0, i)[maxH - 1][maxW - 1]
        if pathLength is not None:
            minPath = min(pathLength, minPath)
    return minPath

def boardWithPathLength(startRow, startCol, m):
    maxH = len(m)
    maxW = len(m[0])
    board = [[None for j in range(maxW)] for i in range(maxH)]
    board[startRow][startCol] = 1

    nodes = [(startRow, startCol)]
    while nodes:
        node = nodes[0]
        nodes = nodes[1:]
        for i in getAllNeighbors(node, m, maxH, maxW):
            if board[i[0]][i[1]] is None:
                board[i[0]][i[1]] = board[node[0]][node[1]] + 1
                nodes.append(i)
    return board

def getAllNeighbors(node, m, maxH, maxW):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in d:
        n = (node[0] + i[0], node[1] + i[1])
        if n[0] >=0 and n[0] < maxH and n[1] >= 0 and n[1] < maxW and not m[n[0]][n[1]]:
            yield n


def getAllMaps(m):
    
    yield m

    for i in range(len(m)):
        for j in range(len(m[i])):
            mCopy = [[col for col in row] for row in m]
            if mCopy[i][j]:
                mCopy[i][j] = 0
                yield mCopy


m = [[0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0]]
m2 = [[0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0]]

print(solution(m))
print(solution(m2))
