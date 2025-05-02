#include "graph.h"
#include <string.h>

void load_map(int map_id, Graph* graph) {
    graph->size = 10;
    for (int i = 0; i < MAX_NODES; i++) {
        for (int j = 0; j < MAX_NODES; j++) {
            graph->matrix[i][j] = INF;
        }
    }

    if (map_id == 1) { // Rajpur Town
        static char* names[] = {"Market", "School", "Hospital", "Park", "Temple",
                                "Station", "Library", "Cafe", "Plaza", "Post Office"};
        for (int i = 0; i < graph->size; i++) {
            graph->nodes[i] = names[i];
        }
        graph->matrix[0][1] = graph->matrix[1][0] = 5;   // Market - School
        graph->matrix[1][2] = graph->matrix[2][1] = 3;   // School - Hospital
        graph->matrix[0][3] = graph->matrix[3][0] = 4;   // Market - Park
        graph->matrix[1][4] = graph->matrix[4][1] = 7;   // School - Temple
        graph->matrix[2][5] = graph->matrix[5][2] = 6;   // Hospital - Station
        graph->matrix[3][4] = graph->matrix[4][3] = 8;   // Park - Temple
        graph->matrix[4][5] = graph->matrix[5][4] = 5;   // Temple - Station
        graph->matrix[3][6] = graph->matrix[6][3] = 9;   // Park - Library
        graph->matrix[5][8] = graph->matrix[8][5] = 4;   // Station - Plaza
        graph->matrix[6][7] = graph->matrix[7][6] = 6;   // Library - Cafe
        graph->matrix[7][8] = graph->matrix[8][7] = 3;   // Cafe - Plaza
        graph->matrix[6][9] = graph->matrix[9][6] = 7;   // Library - Post Office
    } else { // Clock Tower Area
        static char* names[] = {"Clock Tower", "Bank", "Gym", "Mall", "Church",
                                "Bus Stop", "Clinic", "Bakery", "Garden", "Hotel"};
        for (int i = 0; i < graph->size; i++) {
            graph->nodes[i] = names[i];
        }
        graph->matrix[0][1] = graph->matrix[1][0] = 6;   // Clock Tower - Bank
        graph->matrix[1][2] = graph->matrix[2][1] = 4;   // Bank - Gym
        graph->matrix[0][3] = graph->matrix[3][0] = 5;   // Clock Tower - Mall
        graph->matrix[1][4] = graph->matrix[4][1] = 8;   // Bank - Church
        graph->matrix[2][5] = graph->matrix[5][2] = 7;   // Gym - Bus Stop
        graph->matrix[3][4] = graph->matrix[4][3] = 9;   // Mall - Church
        graph->matrix[4][5] = graph->matrix[5][4] = 3;   // Church - Bus Stop
        graph->matrix[3][6] = graph->matrix[6][3] = 6;   // Mall - Clinic
        graph->matrix[5][8] = graph->matrix[8][5] = 5;   // Bus Stop - Garden
        graph->matrix[6][7] = graph->matrix[7][6] = 4;   // Clinic - Bakery
        graph->matrix[7][8] = graph->matrix[8][7] = 3;   // Bakery - Garden
        graph->matrix[6][9] = graph->matrix[9][6] = 8;   // Clinic - Hotel
    }
}

void get_node_positions(int map_id, float positions[][2]) {
    if (map_id == 1) { // Rajpur Town
        float pos[10][2] = {
            {50, 50},   // Market
            {150, 50},  // School
            {250, 50},  // Hospital
            {50, 150},  // Park
            {150, 150}, // Temple
            {250, 150}, // Station
            {50, 250},  // Library
            {150, 250}, // Cafe
            {250, 250}, // Plaza
            {350, 250}  // Post Office
        };
        memcpy(positions, pos, sizeof(pos));
    } else { // Clock Tower Area
        float pos[10][2] = {
            {50, 50},   // Clock Tower
            {150, 50},  // Bank
            {250, 50},  // Gym
            {50, 150},  // Mall
            {150, 150}, // Church
            {250, 150}, // Bus Stop
            {50, 250},  // Clinic
            {150, 250}, // Bakery
            {250, 250}, // Garden
            {350, 250}  // Hotel
        };
        memcpy(positions, pos, sizeof(pos));
    }
}