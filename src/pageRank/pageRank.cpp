#include "pageRank.hpp"
#include "graph.cpp"

void pageRank(float alpha, int iterations) {

}

int main() {
    int numVertices = 5;
    Graph g(numVertices);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(3, 4);

    g.printGraph();
    std::cout << g.num_edges(0) << std::endl;

    // two parameters: smoothing factor, number of iterations
    

    return 0;
}
