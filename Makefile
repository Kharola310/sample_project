CC = gcc
CFLAGS = -Wall -Iinclude
SRC = src/main.c src/graph.c src/dijkstra.c src/fileio.c
OBJ = $(SRC:.c=.o)
EXEC = planner

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	del $(OBJ) $(EXEC).exe