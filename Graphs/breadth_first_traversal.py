class Queue:
  def __init__(self):
    self.l = []
  
  def push(self, val):
    self.l.append(val)
  
  def pop(self):
    return(self.l.pop(0))
  
  def peek(self):
    return (self.l[0])
  
  def isEmpty(self):
    return (len(self.l) == 0)

class Graph:
  def __init__(self, num_vertices):
    self.num_vtx = num_vertices
    self.visited = [0]*num_vertices
    self.queue = Queue()
    self.adj_mtx = []
    for _ in range(self.num_vtx):
      self.adj_mtx.append([0]*self.num_vtx)
    
  
  def add_edge(self, src, dst):
    self.adj_mtx[src][dst] = 1
  
  
  def breadth_first_search(self, vtx):
    #print("pushing into the queue: ", vtx)
    self.queue.push(vtx)
    while(self.queue.isEmpty() == False):
      cur_vtx = self.queue.pop()
      print(cur_vtx)
      self.visited[cur_vtx] = 1
      for i in range(0, self.num_vtx):
        if (self.adj_mtx[cur_vtx][i] == 1 and self.visited[i] == 0):
          self.visited[i] = 1
          #print("cur_vtx: {} vtx pushing: {}".format(cur_vtx, i))
          self.queue.push(i)
      



def main():
  g = Graph(8)
  g.add_edge(0,1)
  g.add_edge(1,2)
  g.add_edge(1,3)
  g.add_edge(2,4)
  g.add_edge(3,4)
  g.add_edge(4,5)
  g.add_edge(3,6)
  g.add_edge(4,7)
  print("Doing Breadth First Search Traversal")
'''
  0
  |
  v
  1--> 2
  |    |
  v    v
  3--> 4--> 5
  |    |
  v    v
  6    7
'''



  g.breadth_first_search(0)

if __name__ == "__main__":
  main()
