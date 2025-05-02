#include "dijkstra.h"
#include <stdio.h>
#include <string.h>
#include <limits.h>

void dijkstra(Graph* graph, int start, int end, char* path, int* distance) {
    int dist[MAX_NODES];
    int prev[MAX_NODES];
    int visited[MAX_NODES];
    int i, u, min_dist;

    for (i = 0; i < graph->size; i++) {
        dist[i] = INF;
        prev[i] = -1;
        visited[i] = 0;
    }

    dist[start] = 0;

    for (i = 0; i < graph->size; i++) {
        min_dist = INF;
        u = -1;
        for (int j = 0; j < graph->size; j++) {
            if (!visited[j] && dist[j] < min_dist) {
                min_dist = dist[j];
                u = j;
            }
        }

        if (u == -1 || u == end) break;

        visited[u] = 1;

        for (int v = 0; v < graph->size; v++) {
            if (!visited[v] && graph->matrix[u][v] != INF) {
                int alt = dist[u] + graph->matrix[u][v];
                if (alt < dist[v]) {
                    dist[v] = alt;
                    prev[v] = u;
                }
            }
        }
    }

    if (dist[end] == INF) {
        strcpy(path, "No path exists");
        *distance = 0;
        return;
    }

    *distance = dist[end];
    char temp[256] = "";
    int current = end;
    while (current != -1) {
        char node[32];
        snprintf(node, sizeof(node), "%s", graph->nodes[current]);
        if (strlen(temp) == 0) {
            strcpy(temp, node);
        } else {
            char new_path[256];
            snprintf(new_path, sizeof(new_path), "%s -> %s", node, temp);
            strcpy(temp, new_path);
        }
        current = prev[current];
    }
    strcpy(path, temp);
}