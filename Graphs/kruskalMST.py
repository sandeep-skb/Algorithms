import sys
class PriorityQueue:
  def __init__(self):
    self.pq = {}
  
  def push(self, vtx, val):
    self.pq[vtx] = val
  
  def deleteMin(self):
    min_val = min(self.pq.values())
    for key in self.pq.keys():
      if self.pq[key] == min_val:
        vtx = key
        break
    self.pq.pop(vtx)
    return vtx
    
  
  def IsEmpty(self):
    return (len(self.pq) == 0)
  
class Graph:
  def __init__(self, vertices):
    self.num_vtx = vertices
    self.edges = []
    self.parent = [i for i in range(self.num_vtx)]
    self.rank = [0 for _ in range(self.num_vtx)]

  def addEdge(self, u, v , w):
    self.edges.append([u,v,w])

  def findParent(self, vtx):
    if self.parent[vtx] == vtx:
      return vtx
    return self.findParent(self.parent[vtx])
    
  def setParent(self, u, v):
    parent_u = self.findParent(u)
    parent_v = self.findParent(v)
    if self.rank[u] >= self.rank[v]:
      self.parent[v] = parent_u
      #print("Setting the parent of {} to {}".format(v, parent_u))
    else:
      self.parent[u] = parent_v
      #print("Setting the parent of {} to {}".format(u, parent_v))
    self.rank[u] += 1
    self.rank[v] += 1

  def KruskalMST(self):
    mst_set = []
    self.edges = sorted(self.edges, key=lambda x: x[2])
    
    e = 0
    
    while(e < self.num_vtx-1):
      u, v, w = self.edges.pop(0)
      parent_u = self.findParent(u)
      #print("parent of {} is {}".format(u, parent_u))
      parent_v = self.findParent(v)
      #print("parent of {} is {}".format(v, parent_v))
      if parent_u != parent_v:
        e += 1
        mst_set.append([u, v, w])
        
        self.setParent(u, v)

    for x in mst_set:
      print("distance from {} to {} is {}".format(x[0], x[1], x[2]))

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.KruskalMST()  
