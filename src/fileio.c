#include "fileio.h"
#include <stdio.h>
#include <time.h>
#include <string.h>

void save_record(char* map_name, char* path, int distance, char* desc) {
    FILE* fp = fopen("data\\history.txt", "a");
    if (!fp) return;

    time_t t = time(NULL);
    struct tm* tm = localtime(&t);
    char date[32];
    strftime(date, sizeof(date), "%Y-%m-%d %H:%M", tm);

    fprintf(fp, "%s | %s | %s | Distance: %d | Desc: %s\n", date, map_name, path, distance, desc);
    fclose(fp);
}

void read_records(char* buffer, int max_len) {
    FILE* fp = fopen("data\\history.txt", "r");
    if (!fp) {
        strcpy(buffer, "No records found");
        return;
    }

    buffer[0] = '\0';
    char line[256];
    while (fgets(line, sizeof(line), fp) && max_len > strlen(buffer) + strlen(line)) {
        strcat(buffer, line);
    }
    fclose(fp);
}