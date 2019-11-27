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
    bool isCyclic();
};

void Graph::addEdge(int src, int dst){
    adj_list[src].push_back(dst);
    incoming[dst]++;
}

bool Graph::isCyclic(){
    queue<int> myqueue;
    int count = 0;
    for (int i =0; i < incoming.size(); ++i){
        if (incoming[i] == 0){
            myqueue.push(i);
        }
    }
    
    while(!myqueue.empty()){
        int src = myqueue.front();
        myqueue.pop();
        //cout << "src: " << src << endl;
        count++;
        for (auto dst : adj_list[src]){
            if (--incoming[dst] == 0){
                myqueue.push(dst);
            }
        }
    }
    
    if (count == numVertex){
        return false;
    }
    else{
        return true;
    }
}

int main()
{
    Graph g(4); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    //g.addEdge(2, 0); 
    g.addEdge(2, 3); 
    //g.addEdge(3, 3); 
  
    if(g.isCyclic()) 
        cout << "Graph contains cycle"; 
    else
        cout << "Graph doesn't contain cycle"; 
    return 0; 

}
