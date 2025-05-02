#ifndef GRAPH_H
#define GRAPH_H

#define MAX_NODES 10
#define INF 9999

typedef struct {
    int matrix[MAX_NODES][MAX_NODES];
    char* nodes[MAX_NODES];
    int size;
} Graph;

void load_map(int map_id, Graph* graph);
void get_node_positions(int map_id, float positions[][2]);

#endif