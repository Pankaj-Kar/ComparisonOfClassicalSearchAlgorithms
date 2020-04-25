import numpy as np
import queue
import copy
import heapq
import math
import time
cst = 0
discovered = []
states = []
visited = []
size = 0
flag = False
depth = 0
goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class node:
    def __init__(self, state, parent, moves):
        self.state = state
        self.parent = parent
        self.moves = moves
        self.depth = math.inf

    def __lt__(self, other):
        return self.depth < other.depth


def move(board, i, j, a, b):
    #print(i , j, a, b)
    board[i][j] = board[a][b]
    board[a][b] = 0


def findBlank(board, size):
    # print(board)
    for i in range(size):
        for j in range(size):
            # print(board[i][j])
            if board[i][j] == 0:
                return (i, j)


def Up(board, i, j, size):
    tmp = copy.deepcopy(board)
    if i == 0:
        return False
    else:
        move(tmp, i, j, i-1, j)
    #print(board, "he")
    # print(tmp)
    return tmp


def Down(board, i, j, size):
    tmp = copy.deepcopy(board)
    if i == size-1:
        return False
    else:
        move(tmp, i, j, i+1, j)
    return tmp


def Left(board, i, j, size):
    tmp = copy.deepcopy(board)
    if j == 0:
        return False
    else:
        move(tmp, i, j, i, j-1)
    return tmp


def Right(board, i, j, size):
    tmp = copy.deepcopy(board)
    if j == size-1:
        return False
    else:
        move(tmp, i, j, i, j+1)
    return tmp


def getNumberOfMisplacedTiles(given, final, size):
    tiles = 0
    for i in range(size):
        for j in range(size):
            if given[i][j] != final[i][j] and given[i][j] != 0:
                tiles += 1
    return tiles


def getManhattanDistance(given, gg, size):
    distance = 0
    for i in range(size):
        for j in range(size):
            #print(given, gg)
            if given[i][j] != gg[i][j]:
                if given[i][j] == 1:
                    distance += abs(i-0)+abs(j-0)
                if given[i][j] == 2:
                    distance += abs(i-0)+abs(j-1)
                if given[i][j] == 3:
                    distance += abs(i-0)+abs(j-2)
                if given[i][j] == 4:
                    distance += abs(i-1)+abs(j-0)
                if given[i][j] == 5:
                    distance += abs(i-1)+abs(j-1)
                if given[i][j] == 6:
                    distance += abs(i-1)+abs(j-2)
                if given[i][j] == 7:
                    distance += abs(i-2)+abs(j-0)
                if given[i][j] == 8:
                    distance += abs(i-2)+abs(j-1)
                if given[i][j] == 0:
                    distance += abs(i-2)+abs(j-2)
    return distance


def bfs(nd, size, bfsNode):
    Q = queue.Queue()
    Q.put(nd)

    vis = []
    vis.append(nd)
    cost = 0
    nd.depth = 0
    while Q.not_empty:
        cost += 1
        temp = Q.get()
        (x, y) = findBlank(temp.state, size)
        if temp.state == goalState:
            print(f'GOALLLL!! at cost {cost}')
            # print(temp.depth)
            return cost
        u = Up(temp.state, x, y, size)
        #print(u, "u")
        #print(temp.state, "temp")
        d = Down(temp.state, x, y, size)
        #print(d, "d")
        #print(temp.state, "temp")
        l = Left(temp.state, x, y, size)
        #print(l, "l")
        #print(temp.state, "temp")
        r = Right(temp.state, x, y, size)
        #print(r, "r")
        #print(temp.state, "temp")

        #print(u,d,l,r, vis, "this")

        if u != False and u not in vis:
            nod = node(u, temp.state, cost)
            nod.depth = temp.depth+1
            vis.append(u)
            Q.put(nod)
        if d != False and d not in vis:
            nod = node(d, temp.state, cost)
            vis.append(d)
            nod.depth = temp.depth+1
            Q.put(nod)

        if l != False and l not in vis:
            nod = node(l, temp.state, cost)
            vis.append(l)
            nod.depth = temp.depth+1
            Q.put(nod)
        if r != False and r not in vis:
            nod = node(r, temp.state, cost)
            vis.append(r)
            nod.depth = temp.depth+1
            Q.put(nod)


def ucs(nd, size):
    # Q=queue.Queue()
    # Q.put(nd)
    Q = []
    Q.append(nd)
    heapq.heapify(Q)

    nd.depth = 0
    vis = []
    vis.append(nd)
    nd.depth = 1
    cost = 0
    while True:
        if not Q:
            # print("Nothing")
            return
        cost += 1
        temp = heapq.heappop(Q)
        (x, y) = findBlank(temp.state, size)
        if temp.state == goalState:
            print(f'GOALLLL!! at cost {cost}')
            # print(temp.depth)
            return cost
            break
        u = Up(temp.state, x, y, size)
       # print(u, "u")
        #print(temp.state, "temp")
        d = Down(temp.state, x, y, size)
       # print(d, "d")
        #print(temp.state, "temp")
        l = Left(temp.state, x, y, size)
       # print(l, "l")
        #print(temp.state, "temp")
        r = Right(temp.state, x, y, size)
       # print(r, "r")
        #print(temp.state, "temp")

        #print(u,d,l,r, vis, "this")

        if u != False and u not in vis:
            adjNod = node(u, temp.state, cost)
            if adjNod.depth > (temp.depth+1):
                adjNod.depth = temp.depth+1
            vis.append(u)
            Q.append(adjNod)
            heapq.heapify(Q)

        if d != False and d not in vis:
            adjNod = node(d, temp.state, cost)
            if adjNod.depth > (temp.depth+1):
                adjNod.depth = temp.depth+1
            vis.append(d)
            Q.append(adjNod)
            heapq.heapify(Q)

        if l != False and l not in vis:
            adjNod = node(l, temp.state, cost)
            if adjNod.depth > (temp.depth+1):
                adjNod.depth = temp.depth+1
            vis.append(l)
            Q.append(adjNod)
            heapq.heapify(Q)

        if r != False and r not in vis:
            adjNod = node(r, temp.state, cost)
            if adjNod.depth > (temp.depth+1):
                adjNod.depth = temp.depth+1
            vis.append(r)
            Q.append(adjNod)
            heapq.heapify(Q)


def aStar(nd, size, g, h, cst):
    f1, f2, f3, f4 = math.inf, math.inf, math.inf, math.inf

    discovered.append(nd)
    states.append(nd.state)

    temp = nd
    (x, y) = findBlank(temp.state, size)

    u = Up(temp.state, x, y, size)
   # print(u, "u")
    if u != False and u not in states:
        cst += 1
        f1 = g+1 + getNumberOfMisplacedTiles(u, goalState, size)
        if getNumberOfMisplacedTiles(u, goalState, size) == 0:
            print("Goalllllll: Node found", f1, g+1,
                  getNumberOfMisplacedTiles(u, goalState, size))
            # print(temp.depth)
            return cst

    d = Down(temp.state, x, y, size)
    #print(d, "d")
    if d != False and d not in states:
        cst += 1
        f2 = g+1 + getNumberOfMisplacedTiles(d, goalState, size)
        if getNumberOfMisplacedTiles(d, goalState, size) == 0:
            print("Goalllllll: Node found", f2, g+1,
                  getNumberOfMisplacedTiles(d, goalState, size))
            # print(temp.depth)
            return cst

    l = Left(temp.state, x, y, size)
   # print(l, "l")
    if l != False and l not in states:
        cst += 1
        f3 = g+1 + getNumberOfMisplacedTiles(l, goalState, size)
        if getNumberOfMisplacedTiles(l, goalState, size) == 0:
            print("Goalllllll: Node found", f3, g+1,
                  getNumberOfMisplacedTiles(l, goalState, size))
            # print(temp.depth)
            return cst

    r = Right(temp.state, x, y, size)
   # print(r, "r")
    if r != False and r not in states:
        cst += 1
        f4 = g+1 + getNumberOfMisplacedTiles(r, goalState, size)
        if getNumberOfMisplacedTiles(r, goalState, size) == 0:
            print("Goalllllll: Node found", f4, g+1,
                  getNumberOfMisplacedTiles(r, goalState, size))
            # print(temp.depth)
            return cst

    take = min(f1, f2, f3, f4)
    #print(take, f1, f2, f3, f4)

    if take == f1:

        nodeUp = node(u, nd.state, g+1)
        # nodeUp.depth+=1
        aStar(nodeUp, size, g+1, getNumberOfMisplacedTiles(u, goalState, size), cst)
        return cst

    if take == f2:
        # print("DDDDD")
        nodeDown = node(d, nd.state, g+1)
        # nodeDown.depth+=1
        aStar(nodeDown, size, g+1,
              getNumberOfMisplacedTiles(d, goalState, size), cst)
        return cst

    if take == f3:
        nodeLeft = node(l, nd.state, g+1)
        # nodeLeft.depth+=1
        aStar(nodeLeft, size, g+1,
              getNumberOfMisplacedTiles(l, goalState, size), cst)
        return cst
    if take == f4:
        # print("RRRR")
        nodeRight = node(r, nd.state, g+1)
        # nodeRight.depth+=1
        aStar(nodeRight, size, g+1,
              getNumberOfMisplacedTiles(r, goalState, size), cst)
        return cst


def aStarManhattan(nd, size, g, h, cst):
    f1, f2, f3, f4 = math.inf, math.inf, math.inf, math.inf

    discovered.append(nd)
    states.append(nd.state)

    temp = nd
    (x, y) = findBlank(temp.state, size)

    u = Up(temp.state, x, y, size)
    #print(u, "u")
    if u != False and u not in states:
        cst += 1
        f1 = g+1 + getManhattanDistance(u, goalState, size)
        if getManhattanDistance(u, goalState, size) == 0:
            print("Goalllllll: Node found", f1, g+1,
                  getManhattanDistance(u, goalState, size))
            return cst

    d = Down(temp.state, x, y, size)
    #print(d, "d")
    if d != False and d not in states:
        cst += 1
        f2 = g+1 + getManhattanDistance(d, goalState, size)
        if getManhattanDistance(d, goalState, size) == 0:
            print("Goalllllll: Node found", f2, g+1,
                  getManhattanDistance(d, goalState, size))
            return cst

    l = Left(temp.state, x, y, size)
    #print(l, "l")
    if l != False and l not in states:
        cst += 1
        f3 = g+1 + getManhattanDistance(l, goalState, size)
        if getManhattanDistance(l, goalState, size) == 0:
            print("Goalllllll: Node found", f3, g+1,
                  getManhattanDistance(l, goalState, size))
            return cst

    r = Right(temp.state, x, y, size)
    #print(r, "r")
    if r != False and r not in states:
        cst += 1
        f4 = g+1 + getManhattanDistance(r, goalState, size)
        if getManhattanDistance(r, goalState, size) == 0:
            # print("RRRRR")
            print("Goalllllll: Node found", f4, g+1,
                  getManhattanDistance(r, goalState, size))
            return cst

    take = min(f1, f2, f3, f4)
    #print(take, f1, f2, f3, f4)

    if take == f1:

        nodeUp = node(u, nd.state, g+1)
        aStarManhattan(nodeUp, size, g+1,
                       getManhattanDistance(u, goalState, size), cst)
        return cst

    if take == f2:
        # print("DDDDD")
        nodeDown = node(d, nd.state, g+1)
        aStarManhattan(nodeDown, size, g+1,
                       getManhattanDistance(d, goalState, size), cst)
        return cst

    if take == f3:
        nodeLeft = node(l, nd.state, g+1)
        aStarManhattan(nodeLeft, size, g+1,
                       getManhattanDistance(l, goalState, size), cst)
        return cst

    if take == f4:
        # print("RRRR")
        nodeRight = node(r, nd.state, g+1)
        aStarManhattan(nodeRight, size, g+1,
                       getManhattanDistance(r, goalState, size), cst)
        return cst


def gbfsManhattan(nd, size, g, h, cst):
    f1, f2, f3, f4 = math.inf, math.inf, math.inf, math.inf

    discovered.append(nd)
    states.append(nd.state)

    temp = nd
    (x, y) = findBlank(temp.state, size)

    u = Up(temp.state, x, y, size)
   # print(u, "u")
    if u != False and u not in states:
        cst += 1
        f1 = getManhattanDistance(u, goalState, size)
        if getManhattanDistance(u, goalState, size) == 0:
            print("Goalllllll: Node found", f1, g+1,
                  getManhattanDistance(u, goalState, size))
            return cst

    d = Down(temp.state, x, y, size)
   # print(d, "d")
    if d != False and d not in states:
        cst += 1
        f2 = getManhattanDistance(d, goalState, size)
        if getManhattanDistance(d, goalState, size) == 0:
            print("Goalllllll: Node found", f2, g+1,
                  getManhattanDistance(d, goalState, size))
            return cst

    l = Left(temp.state, x, y, size)
   # print(l, "l")
    if l != False and l not in states:
        cst += 1
        f3 = getManhattanDistance(l, goalState, size)
        if getManhattanDistance(l, goalState, size) == 0:
            print("Goalllllll: Node found", f3, g+1,
                  getManhattanDistance(l, goalState, size))
            return cst

    r = Right(temp.state, x, y, size)
   # print(r, "r")
    if r != False and r not in states:
        cst += 1
        f4 = getManhattanDistance(r, goalState, size)
        if getManhattanDistance(r, goalState, size) == 0:
            # print("RRRRR")
            print("Goalllllll: Node found", f4, g+1,
                  getManhattanDistance(r, goalState, size))
            return cst

    take = min(f1, f2, f3, f4)
    #print(take, f1, f2, f3, f4)

    if take == f1:

        nodeUp = node(u, nd.state, g+1)
        gbfsManhattan(nodeUp, size, g+1, take, cst)
        return cst

    if take == f2:
        # print("DDDDD")
        nodeDown = node(d, nd.state, g+1)
        gbfsManhattan(nodeDown, size, g+1, take, cst)
        return cst

    if take == f3:
        nodeLeft = node(l, nd.state, g+1)
        gbfsManhattan(nodeLeft, size, g+1, take, cst)
        return cst

    if take == f4:
        # print("RRRR")
        nodeRight = node(r, nd.state, g+1)
        gbfsManhattan(nodeRight, size, g+1, take, cst)
        return cst


def gbfs(nd, size, g, h, cst):
    f1, f2, f3, f4 = math.inf, math.inf, math.inf, math.inf

    discovered.append(nd)
    states.append(nd.state)

    temp = nd
    (x, y) = findBlank(temp.state, size)

    u = Up(temp.state, x, y, size)
   # print(u, "u")
    if u != False and u not in states:
        cst += 1
        f1 = getNumberOfMisplacedTiles(u, goalState, size)
        if getNumberOfMisplacedTiles(u, goalState, size) == 0:
            print("Goalllllll: Node found", f1, g+1,
                  getNumberOfMisplacedTiles(u, goalState, size))
            return cst

    d = Down(temp.state, x, y, size)
   # print(d, "d")
    if d != False and d not in states:
        cst += 1
        f2 = getNumberOfMisplacedTiles(d, goalState, size)
        if getNumberOfMisplacedTiles(d, goalState, size) == 0:
            print("Goalllllll: Node found", f2, g+1,
                  getNumberOfMisplacedTiles(d, goalState, size))
            return cst

    l = Left(temp.state, x, y, size)
   # print(l, "l")
    if l != False and l not in states:
        cst += 1
        f3 = getNumberOfMisplacedTiles(l, goalState, size)
        if getNumberOfMisplacedTiles(l, goalState, size) == 0:
            print("Goalllllll: Node found", f3, g+1,
                  getNumberOfMisplacedTiles(l, goalState, size))
            return cst

    r = Right(temp.state, x, y, size)
   # print(r, "r")
    if r != False and r not in states:
        cst += 1
        f4 = getNumberOfMisplacedTiles(r, goalState, size)
        if getNumberOfMisplacedTiles(r, goalState, size) == 0:
            # print("RRRRR")
            print("Goalllllll: Node found", f4, g+1,
                  getNumberOfMisplacedTiles(r, goalState, size))
            return cst

    take = min(f1, f2, f3, f4)
   # print(take, f1, f2, f3, f4)

    if take == f1:

        nodeUp = node(u, nd.state, g+1)
        gbfs(nodeUp, size, g+1, getNumberOfMisplacedTiles(u, goalState, size), cst)
        return cst

    if take == f2:
        # print("DDDDD")
        nodeDown = node(d, nd.state, g+1)
        gbfs(nodeDown, size, g+1, getNumberOfMisplacedTiles(d, goalState, size), cst)
        return cst

    if take == f3:
        nodeLeft = node(l, nd.state, g+1)
        gbfs(nodeLeft, size, g+1, getNumberOfMisplacedTiles(l, goalState, size), cst)
        return cst

    if take == f4:
        # print("RRRR")
        nodeRight = node(r, nd.state, g+1)
        gbfs(nodeRight, size, g+1, getNumberOfMisplacedTiles(r, goalState, size), cst)
        return cst


def ids(nd, size, cst):
    limit = 0
    moves = 0

    while dlsRecur(nd, limit, moves, size, cst) != True:
        limit += 1
    return limit


def dlsRecur(nd, limit, moves, size, cst):
    moves += 1
    #print(moves, limit)
    if nd.state == goalState:
        print("Found")
        return True

    if limit <= 0:
        #print('Could not find in this limit')
        return False

    (x, y) = findBlank(nd.state, size)

    up = Up(nd.state, x, y, size)
   # print(up, "u")
    if up != False and (up not in visited):
        cst += 1
        visited.append(up)
        adj = node(up, nd.state, moves)
        if dlsRecur(adj, limit - 1, moves, size, cst) == True:
            return True
        visited.remove(up)

    down = Down(nd.state, x, y, size)
   # print(down, "d")
    if down != False and down not in visited:
        cst += 1
        visited.append(down)
        adj = node(down, nd.state, moves)
        if dlsRecur(adj, limit - 1, moves, size, cst) == True:
            return True
        visited.remove(down)

    right = Right(nd.state, x, y, size)
   # print(right, "r")
    if right != False and right not in visited:
        cst += 1
        visited.append(right)
        adj = node(right, nd.state, moves)
        if dlsRecur(adj, limit - 1, moves, size, cst) == True:
            return True
        visited.remove(right)

    left = Left(nd.state, x, y, size)
   # print(left, "l")
    if left != False and left not in visited:
        cst += 1
        visited.append(left)
        adj = node(left, nd.state, moves)
        if dlsRecur(adj, limit - 1, moves, size, cst) == True:
            return True
        visited.remove(left)

    return False


def main():
    sz = int(input("Enter the value of N: "))
    size = sz
    initBoard = [[] for i in range(sz)]
    print("Enter initial board confuguration: ")
    for i in range(sz):
        for j in range(sz):
            x = int(input())
            initBoard[i].append(x)
    print(initBoard, " Initial State")
    nd = node(initBoard, -1, 0)

    print(goalState, " Goal State")
    print('''Which algorithm you want to run?
             1. BFS
             2. UCS
             3. DLS
             4. A*(Misplaced Tiles)
             5. A*(Manhattan Distance)
             6. GBFS(Misplaced Tiles)
             7. GBFS(Manhattan Distance)
             8. IDS3
             9. ALL3
    '''
          )
    v = int(input("Enter the number of the algorithm."))
    if v == 1:
        start = time.time()
        path = bfs(nd, size, 1)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        print(f"BFS time: {endd-start} Path : {path}")
        

    if v == 2:
        start = time.time()
        path = ucs(nd, size)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        print(f"UCS time: {endd-start} Path : {path}")

    if v == 3:
        start = time.time()
        dlsRecur(nd, 100, 0, size)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        print(f"DLS time: {endd-start} ")

    if v == 4:
        start = time.time()
        nd.depth = 0
        path = aStar(nd, size, 0, 0, 0)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        print(f"a* time: {endd-start} Path : {path}")

    if v == 5:
        cst = 0
        start = time.time()
        path = aStarManhattan(nd, size, 0, 0, 0)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
       # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        # fn.close
       # f.close
        #fnds=open("nodes.txt", "a")
        #fnds.write(" ")
        # fnds.write(str(path))
        # fnds.close
        print(f"a* man time: {endd-start} Path : {path}")

    if v == 6:
        start = time.time()
        path = gbfs(nd, size, 0, 0, 0)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        #fnds=open("nodes.txt", "a")
        #fnds.write(" ")
        # fnds.write(str(path))
        # fnds.close
        print(f"GBFS time: {endd-start} Path : {path}")

    if v == 7:
        cst = 0
        start = time.time()
        path = gbfsManhattan(nd, size, 0, 0, 0)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        # fn.close
        # f.close
        #fnds=open("nodes.txt", "a")
        # fnds.write(str(path))
        #fnds.write(" ")
        # fnds.close
        print(f"GBFS Man time: {endd-start} Path : {path}")

    if v == 8:
        cst = 0
        start = time.time()
        path = ids(nd, size, 0)
        endd = time.time()
        #f=open("time.txt", "a")
        #fn=open("path.txt", "a")
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        # fn.close
        # f.close
        #fnds=open("nodes.txt", "a")
        #fnds.write(" ")
        # fnds.write(str(path))
        # fnds.close
        print(f"IDS time: {endd-start} Path : {path}")

    # For running all algo
    if v == 9:
        #f=open("time.txt", "a")
        nd.depth = 0
        start = time.time()
        path = bfs(nd, size, 1)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        #fn=open("path.txt", "a")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds=open("nodes.txt", "a")
        # fnds.write(str(path))
        print(f"1. BFS time: {endd-start} Path : {path}")
        #print("Bfs Node ", bfsNode)

        nd.depth = 0
        start = time.time()
        path = ucs(nd, size)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"2. UCS time: {endd-start} Path : {path}")

        nd.depth = 0
        start = time.time()
        dlsRecur(nd, 10, 0, size, 0)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"3. DLS time: {endd-start} Path : {path}")

        start = time.time()
        nd.depth = 0
        cst = 0
        path = aStar(nd, size, 0, 0, 0)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"4. a* time: {endd-start} Path : {path}")

        states.clear()
        discovered.clear()
        nd.depth = 0
        cst = 0
        start = time.time()
        path = aStarManhattan(nd, size, 0, 0, 0)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"5. a* man time: {endd-start} Path : {path}")

        states.clear()
        discovered.clear()
        nd.depth = 0
        cst = 0
        start = time.time()
        path = gbfs(nd, size, 0, 0, 0)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"6. GBFS time: {endd-start} Path : {path}")

        states.clear()
        discovered.clear()
        nd.depth = 0
        cst = 0
        start = time.time()
        path = gbfsManhattan(nd, size, 0, 0, 0)
        endd = time.time()
        # f.write(str(endd-start))
        #f.write(" ")
        # fn.write(str(path))
        #fn.write(" ")
        #fnds.write(" ")
        # fnds.write(str(path))
        print(f"7. GBFS Man time: {endd-start} Path : {path}")
        # f.close()
        # fn.close()
        # fnds.close()


main()
