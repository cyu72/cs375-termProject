#include <iostream>
#include <vector>

class Graph {
private:
    int V; // Number of vertices
    std::vector<std::vector<int>> adjMatrix;

public:
    Graph(int vertices) : V(vertices), adjMatrix(vertices, std::vector<int>(vertices, 0)) {
    }

    void addEdge(int u, int v) {
        // Add an edge from vertex u to vertex v
        adjMatrix[u][v] = 1;
    }

    void printGraph() {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                std::cout << adjMatrix[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    int num_edges(int u){
        return adjMatrix[u].size();
    }
};
