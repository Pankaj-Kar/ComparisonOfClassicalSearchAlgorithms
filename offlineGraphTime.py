import matplotlib.pyplot as plt
import math
f=open("time.txt","r")
lines=f.readlines()
bfs=[]
for x in lines:
    v = x.split(' ')[0]
    bfs.append(float(v))

ucs=[]
for x in lines:
    v = x.split(' ')[1]
    ucs.append(float(v))

dls=[]
for x in lines:
    v = x.split(' ')[2]
    dls.append(float(v))

astar=[]
for x in lines:
    v = x.split(' ')[3]
    astar.append(float(v))

astarMan=[]
for x in lines:
    v = x.split(' ')[4]
    astarMan.append(float(v))

gb=[]
for x in lines:
    v = x.split(' ')[5]
    gb.append(float(v))

gbMan=[]
for x in lines:
    v = x.split(' ')[6]
    gbMan.append(float(v))

ids=[]
for x in lines:
    v = x.split(' ')[7]
    ids.append(float(v))
f.close()

x1 = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x1, bfs, label = "BFS")
plt.plot(x1, ucs, label = "UCS")
plt.plot(x1, dls, label = "DLS")
plt.plot(x1, astar, label = "A*")
plt.plot(x1, astarMan, label = "A* MD")
plt.plot(x1, gb, label = "GBFS")
plt.plot(x1, gbMan, label = "GBFS MD")
plt.plot(x1, ids, label = "IDS")
plt.xlabel("Steps for BFS")
plt.ylabel("TIME")
plt.title("GRAPH 1 (TIME vs STEPS)")
plt.legend()
plt.show()