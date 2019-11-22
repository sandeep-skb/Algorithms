#include <iostream>
#include <list>
#include <unordered_set>
#include <stack>
using namespace std;

class Graph{
  int num_vertex;
  list<int> *adj_list;
  void dfs(int v, unordered_set<int> &visited, stack<int>& mystack);
public:
  Graph(int n);
  void addEdge(int in, int out);
  void topologicalSort();
};

Graph::Graph(int n){
    num_vertex = n;
    adj_list = new list<int>[num_vertex];
}

void Graph::addEdge(int in, int out){
    adj_list[in].push_back(out);
}

void Graph::topologicalSort(){
    unordered_set<int> visited;
    stack<int> mystack;
    for (int i=0; i<num_vertex; ++i){
        if (visited.find(i) == visited.end()){
            dfs(i, visited, mystack);
        }
    }
    
    while(!mystack.empty()){
        cout << mystack.top() << " ";
        mystack.pop();
    }
}

void Graph::dfs(int v, unordered_set<int> &visited, stack<int>& mystack){
    visited.insert(v);
    for (auto it=adj_list[v].begin(); it != adj_list[v].end(); ++it){
        if (visited.find(*it) == visited.end()){
            dfs(*it, visited, mystack);
        }
    }
    mystack.push(v);
}


int main()
{
    
    Graph g(6); 
    g.addEdge(5, 2); 
    g.addEdge(5, 0); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1); 
  
    cout << "Following is a Topological Sort of the given graph \n"; 
    g.topologicalSort(); 
    return 0;
}
