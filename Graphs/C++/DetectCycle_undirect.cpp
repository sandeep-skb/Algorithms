// DFS approach with parent 

#include <iostream>
#include <vector>
#include <queue>
using namespace std;


class Graph{
    int numVertex;
    vector<vector<int>> adj_list;
    vector<int> visited;
    
public:
    Graph(int numVertex) : numVertex{numVertex}, adj_list(numVertex, vector<int> ()), visited (numVertex,0) {}
    void addEdge(int, int);
    bool isCyclic();
    bool dfs(int, int);
};

void Graph::addEdge(int src, int dst){
    adj_list[src].push_back(dst);
}

bool Graph::isCyclic(){
    for (int i=0; i < numVertex; ++i){
        if (!visited[i] && dfs(i, -1)){
            return true;
        }
    }
    return false;
}

bool Graph::dfs(int src, int parent){
    visited[src] = 1;
    for (auto dst: adj_list[src]){
        if (visited[dst] && parent != dst)
            return true;
        else if (visited[dst])
            continue;
        else if (dfs(dst, src))
            return true;
    }
    return false;
}


int main()
{
    Graph g1(5); 
    g1.addEdge(1, 0); 
    g1.addEdge(0, 2); 
    g1.addEdge(2, 1); 
    g1.addEdge(0, 3); 
    g1.addEdge(3, 4); 
    g1.isCyclic()? cout << "Graph contains cycle\n": 
                   cout << "Graph doesn't contain cycle\n"; 
  
    Graph g2(3); 
    g2.addEdge(0, 1); 
    g2.addEdge(1, 2); 
    g2.isCyclic()? cout << "Graph contains cycle\n": 
                   cout << "Graph doesn't contain cycle\n"; 
        
        
    return 0; 

}
