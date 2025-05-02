#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "graph.h"
#include "dijkstra.h"
#include "fileio.h"

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <command> [args]\n", argv[0]);
        return 1;
    }

    Graph graph;
    char path[256];
    int distance;

    if (strcmp(argv[1], "find") == 0 && argc == 5) {
        int map_id = atoi(argv[2]);
        int start = atoi(argv[3]);
        int end = atoi(argv[4]);
        load_map(map_id, &graph);
        dijkstra(&graph, start, end, path, &distance);
        printf("%s\n%d\n", path, distance);
    } else if (strcmp(argv[1], "save") == 0 && argc == 6) {
        save_record(argv[2], argv[3], atoi(argv[4]), argv[5]);
        printf("Record saved\n");
    } else if (strcmp(argv[1], "read") == 0) {
        char buffer[4096];
        read_records(buffer, sizeof(buffer));
        printf("%s\n", buffer);
    } else {
        printf("Invalid command\n");
        return 1;
    }

    return 0;
}