#include <iostream>
#include <vector>
#include <stack>
using namespace std;


class Graph{
    int numVertex;
    vector<vector<int>> adj_list;
    vector<int> visited;
    
public:
    Graph(int numVertex) : numVertex{numVertex}, adj_list(numVertex, vector<int> ()), visited (numVertex,0) {}
    void addEdge(int, int);
    void topologicalSort();
    void dfs(int, stack<int>&);
};

void Graph::addEdge(int src, int dst){
    adj_list[src].push_back(dst);
}


void Graph::topologicalSort(){
    stack<int> mystack;
    for (int i=0; i < numVertex; ++i){
        if (!visited[i]){
            dfs(i, mystack);
        }
    }
    
    while(!mystack.empty()){
        cout << mystack.top() << " " ;
        mystack.pop();
    }
    
}

void Graph::dfs(int src, stack<int>& mystack){
    visited[src] = 1;
    for (auto dst : adj_list[src]){
        if (!visited[dst])
            dfs(dst, mystack);
    }
    mystack.push(src);
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
