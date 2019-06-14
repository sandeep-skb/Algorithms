class Stack:
  def __init__(self):
    self.l = []
  
  def push(self, val):
    self.l.insert(0, val)
  
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
    self.stack = Stack()
    self.adj_mtx = []
    for _ in range(self.num_vtx):
      self.adj_mtx.append([0]*self.num_vtx)
    
  
  def add_edge(self, src, dst):
    self.adj_mtx[src][dst] = 1
  
  

  def do_topological_sort(self, vtx):
    self.visited[vtx] = 1
    for i in range(self.num_vtx):
      if (self.adj_mtx[vtx][i] == 1 and self.visited[i] == 0):
        self.do_topological_sort(i)
    self.stack.push(vtx)


  def topological_sort(self):
    for i in range(self.num_vtx):
      if self.visited[i] == 0:
        self.do_topological_sort(i)
    
    while(self.stack.isEmpty() == False):
      print(self.stack.pop())
  

      



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

  print("Doing Topological Sorting")
  g.topological_sort()

if __name__ == "__main__":
  main()
