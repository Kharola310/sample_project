Smart Delivery Route Planner
A PBL project for finding optimal delivery routes in a small town using Dijkstra’s algorithm (C) and a Tkinter GUI (Python).
Features

Select from predefined maps (10 locations each).
View maps on a Tkinter canvas.
Find shortest paths using Dijkstra’s algorithm.
Save and view delivery records (path, distance, description).

Setup

Prerequisites:
GCC (for compiling C code)
Python 3 with Tkinter (pip install tk)


Clone the Repository:git clone https://github.com/kharola889/sem_project.git
cd sem_project


Compile C Code:make


Run the GUI:python gui/interface.py



Usage

Select a map (e.g., Rajpur Town).
View the map on the canvas.
Choose start and end locations.
Click "Find Route" to see the shortest path.
Save the delivery record with a description.
View past records via the "View Records" button.

Folder Structure

src/: C source files (graph, Dijkstra, file I/O).
include/: C header files.
gui/: Python GUI code.
data/: Delivery records (history.txt).
tests/: Test inputs.

Example

Map: Rajpur Town
Start: Market, End: Hospital
Output: Market -> School -> Hospital, Distance: 8
Saved Record: 2025-05-02 10:30 | Rajpur Town | Market -> School -> Hospital | Distance: 8 | Delivered package

