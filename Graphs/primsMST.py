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
    self.graph = [[0 for _ in range(vertices)] 
                  for _ in range(vertices)]
    self.pqueue = PriorityQueue()
    self.distance = [sys.maxsize] * self.num_vtx
    self.path = [0]*self.num_vtx

  def find_shortest_dist(self, idx):
    for col in range(self.num_vtx):
      if (self.graph[idx][col] != 0):
        temp_dist = self.graph[idx][col]
        if (temp_dist < self.distance[col]):
          self.distance[col] = temp_dist
          self.pqueue.push(col, temp_dist)
          self.path[col] = idx


  def primMST(self, src):
    orig_set = [i for i in range(self.num_vtx)]
    mst_set = []
    self.distance[src] = 0
    self.pqueue.push(src, self.distance[src])
    while(self.pqueue.IsEmpty() != True):
      idx = self.pqueue.deleteMin()
      if (idx not in mst_set):
        mst_set.append(idx)
        orig_set.remove(idx)
        self.find_shortest_dist(idx)
    
    for i in range(len(self.distance)):
      print("distance from {} to {} is {}".format(self.path[i], i, self.distance[i]))


def main():
  g = Graph(5) 
  g.graph = [ [0, 2, 0, 6, 0], 
              [2, 0, 3, 8, 5], 
              [0, 3, 0, 0, 7], 
              [6, 8, 0, 0, 9], 
              [0, 5, 7, 9, 0]] 

  g.primMST(0); 
  
if __name__ == "__main__":
  main()
