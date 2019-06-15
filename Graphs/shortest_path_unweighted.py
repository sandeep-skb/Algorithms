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
    self.distance = [-1]*num_vertices
    self.path = [-1]*num_vertices
    
  def add_edge(self, src, dst):
    self.adj_mtx[src][dst] = 1
    
  def shortest_path_util(self, vtx):
    #print("pushing into the queue: ", vtx)
    self.queue.push(vtx)
    self.distance[vtx] = 0
    while(self.queue.isEmpty() == False):
      cur_vtx = self.queue.pop()
      self.visited[cur_vtx] = 1
      end = True
      for i in range(0, self.num_vtx):
        if (self.adj_mtx[cur_vtx][i] == 1 and self.visited[i] == 0):
          self.visited[i] = 1
          self.distance[i] = self.distance[cur_vtx] + 1
          self.path[i] = cur_vtx
          self.queue.push(i)
          end = False
      #Break the while loop at the first dead end. This is the shortest route.
      if end == True:
        break
  
  def calc_shortest_path(self, vtx):
    self.shortest_path_util(vtx)
    #Get the index of the dead end node.
    idx = self.distance.index(max(self.distance))
    
    while(idx != vtx):
      print("{}<--".format(idx), end="")
      idx = self.path[idx]
    print(vtx)

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
  print("Calculating shortest path from 0")
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
  # Specify the starting point from where to calculate the shortest path.
  g.calc_shortest_path(0)

if __name__ == "__main__":
  main()
