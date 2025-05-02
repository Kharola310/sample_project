#ifndef FILEIO_H
#define FILEIO_H

void save_record(char* map_name, char* path, int distance, char* desc);
void read_records(char* buffer, int max_len);

#endif