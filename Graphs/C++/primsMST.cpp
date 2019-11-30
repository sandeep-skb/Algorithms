#include <iostream>
#include <climits>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Graph{
    int numVertex;
    vector<vector<pair<int,int>>> adj_list;
    vector<int> distance;
    vector<int> parent;
public:
    Graph(int numVertex) : numVertex{numVertex}, distance(numVertex, INT_MAX), parent(numVertex, -1), adj_list(numVertex, vector<pair<int,int>> ()){}
    void addEdge(int, int, int);
    void PrimMST(int);
};

void Graph::addEdge(int src, int dst, int wgt){
    adj_list[src].push_back(make_pair(dst, wgt));
    adj_list[dst].push_back(make_pair(src, wgt));
}

void Graph::PrimMST(int src){
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    unordered_set<int> mst;
    distance[src] = 0;
    pq.push(make_pair(0, src));
    
    while(mst.size() < numVertex){
        auto pair_u = pq.top();
        int d = pair_u.first;
        int u = pair_u.second;
        pq.pop();
        //if (mst.find(u) != mst.end()) continue;
        mst.insert(u);
        cout << "src: " << u << " parent: " << parent[u] << endl;
        for(auto it : adj_list[u]){
            int v = it.first;
            int w = it.second;
            if (mst.find(v) != mst.end()) continue;
            if ((distance[v] == INT_MAX) || (distance[v] > w)) {
                distance[v] = w;
                parent[v] = u;
                pq.push(make_pair(w, v));
                cout << " dst: " << v << " dist: " << distance[v] << endl;
            }
        }
    }
    
    for(int i=0; i < numVertex; i++){
        cout << parent[i] << " -> " << i  << endl;
    }
    
    
}





int main()
{
    Graph g(9);
    g.addEdge(0,1,4);
    g.addEdge(0,7,8);
    g.addEdge(1,7,11);
    g.addEdge(1,2,8);
    g.addEdge(2,3,7);
    g.addEdge(2,5,4);
    g.addEdge(2,8,2);
    g.addEdge(3,4,9);
    g.addEdge(3,5,14);
    g.addEdge(4,5,10);
    g.addEdge(5,6,2);
    g.addEdge(6,8,6);
    g.addEdge(6,7,1);
    g.addEdge(7,8,7);

    cout << "PRIM's MST: " << endl;
    g.PrimMST(0);
    return 0;
}
