/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <list>
#include <unordered_set>
#include <stack>
#include <queue>
using namespace std;

class Graph{
  int num_vertex;
  list<int> *adj_list;
  vector<int> indegree;
public:
  Graph(int n);
  void addEdge(int in, int out);
  void topologicalSort();
};

Graph::Graph(int n) : num_vertex{n}, indegree(n,0) 
{
    adj_list = new list<int>[num_vertex];
    
}

void Graph::addEdge(int in, int out){
    adj_list[in].push_back(out);
    indegree[out]++;
}

void Graph::topologicalSort(){
    
    queue<int> myqueue;
    
    for (int i=0; i < num_vertex; ++i){
        if (indegree[i] == 0){
            myqueue.push(i);
        }
    }
    
    while(!myqueue.empty()){
        int v = myqueue.front();
        cout << v << " " ;
        myqueue.pop();
        for(auto it=adj_list[v].begin(); it!=adj_list[v].end(); ++it){
            indegree[*it]--;
            if (indegree[*it] == 0)
                myqueue.push(*it);
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
