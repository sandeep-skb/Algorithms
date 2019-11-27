// This is the DFS approach.

#include <iostream>
#include <vector>
#include <queue>
using namespace std;


class Graph{
    int numVertex;
    vector<vector<int>> adj_list;
    vector<int> visited;
    vector<int> rec_stack;
    
public:
    Graph(int numVertex) : numVertex{numVertex}, adj_list(numVertex, vector<int> ()), visited (numVertex,0), rec_stack(numVertex, 0) {}
    void addEdge(int, int);
    bool isCyclic();
    bool dfs(int);
};

void Graph::addEdge(int src, int dst){
    adj_list[src].push_back(dst);
}

bool Graph::isCyclic(){
    for (int i=0; i < numVertex; ++i){
        if (!visited[i] && dfs(i)){
            return true;
        }
    }
    return false;
}

bool Graph::dfs(int src){
    rec_stack[src] = 1;
    visited[src] = 1;
    for (auto dst: adj_list[src]){
        if (visited[dst] && rec_stack[dst])
            return true;
        else if (visited[dst])
            continue;
        else if (dfs(dst))
            return true;
    }
    rec_stack[src] = 0;
    return false;
}


int main()
{
    Graph g(4); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3); 
    //g.addEdge(3, 3); 
  
    if(g.isCyclic()) 
        cout << "Graph contains cycle"; 
    else
        cout << "Graph doesn't contain cycle"; 
        
        
    return 0; 

}
