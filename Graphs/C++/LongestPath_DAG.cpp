// A C++ program to find single source longest distances 
// in a DAG 
//https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/


#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <climits>
using namespace std;


class Graph{
    int numVertex;
    vector<vector<pair<int,int> > > adj_list;
    vector<int> distance;
    vector<int> incoming;
    
public:
    Graph(int numVertex) : numVertex{numVertex}, adj_list(numVertex, vector<pair<int,int>> ()), distance (numVertex,INT_MIN), incoming (numVertex, 0) {}
    void addEdge(int, int, int);
    void longestPath(int);
};

void Graph::addEdge(int src, int dst, int w){
    adj_list[src].push_back(make_pair(dst, w));
    incoming[dst]++;
}


void Graph::longestPath(int src){
    
    queue<int> topo_queue;
    queue<int> myqueue;
    for (int i=0 ; i < numVertex; ++i){
        if (incoming[i] == 0)
            myqueue.push(i);
    }
    // Topo sort
    while(!myqueue.empty()){
        int u = myqueue.front();
        myqueue.pop();
        topo_queue.push(u);
        for (auto it : adj_list[u]){
            int v = it.first;
            if (--incoming[v] == 0){
                myqueue.push(v);
            }
        }
    }
        
    distance[src] = 0;
    
    while(!topo_queue.empty()){
        int u = topo_queue.front();
        topo_queue.pop();
        if (distance[u] == INT_MIN) continue;
        for (auto it : adj_list[u]){
            int v = it.first;
            int w = it.second;
            if (distance[v] == INT_MIN){
                distance[v] = w + distance[u];
            }
            else{
                distance[v] = max(distance[v], w + distance[u]);
            }
        }
    }

    cout << "Distance from " << src << ": " ;
    for (auto d : distance){
        if (d == INT_MIN){
            cout << "INT_MIN " ;
        }
        else{
            cout << d << " ";
        }
    }
    
}


int main()
{
    Graph g(6);  
    g.addEdge(0, 1, 5);  
    g.addEdge(0, 2, 3);  
    g.addEdge(1, 3, 6);  
    g.addEdge(1, 2, 2);  
    g.addEdge(2, 4, 4);  
    g.addEdge(2, 5, 2);  
    g.addEdge(2, 3, 7);  
    g.addEdge(3, 5, 1);  
    g.addEdge(3, 4, -1);  
    g.addEdge(4, 5, -2);  
    
    int s = 1;  
    cout << "Following are longest distances from "
            "source vertex "
         << s << " \n";  
    g.longestPath(s);  
        
        
    return 0; 

}
