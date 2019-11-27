/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;


class Graph{
    int numVertex;
    vector<vector<int>> adj_list;
    vector<int> incoming;
    
public:
    Graph(int numVertex) : numVertex{numVertex}, adj_list(numVertex, vector<int> ()), incoming (numVertex,0) {}
    void addEdge(int, int);
    void topologicalSort();
};

void Graph::addEdge(int src, int dst){
    adj_list[src].push_back(dst);
    incoming[dst]++;
}


void Graph::topologicalSort(){
    queue<int> myqueue;
    for(int i=0; i<numVertex; ++i){
        if (incoming[i] == 0)
            myqueue.push(i);
    }
    
    while(!myqueue.empty()){
        int src = myqueue.front();
        myqueue.pop();
        cout << src << " ";
        for (auto dst: adj_list[src]){
            if (--incoming[dst] == 0)
                myqueue.push(dst);
        }
    }
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
