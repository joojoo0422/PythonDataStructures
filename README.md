# Python Data Structures and Algorithms
Implementation of DFS, BFS, A* Search using Stacks and Queues in Python


## Introduction
I've taken the Python Data Structures and Algorithms course in LinkedIn Learning by Robit Andrews. This is a summary of what I've learned and implementations of DFS, BFS, A* search, Stacks and Queues using Python. 

Implementations in this course uses 2D List Data Structure and Matrix Coordinates.

## The Stack Data Structure
- **Stack** is a a data structure in which all insertions and deletions are made at one end, call the top of the stack.
- Stack uses LIFO (Last In, First Out)

Common Stack Operations
- push(item): push item to the top of the stack
- pop(item): remove and return the top item
- peek(item): return the top item without removing it
- is_empty(item): return true if the stack is empty

Implementation
- stack.py

Exercise: Use the Stack class to create a program which reverses a string.
- Solution: reverse_string.py 

## Depth-First Search Algorithm
- Uses Stack in the algorithm
- Does not guarantee finding the shortest path
- Time Complexity: O(N*M) for N is number of rows and N is number of columns

Implementation
- dfs.py

## The Queue Data Structure
- **Queue** is a data structure in which all additions are made in the rear (tail) of the queue, and all removals are made in the front (head) of the queue.
- Queue uses FIFO (First In, First Out)

Common Queue Operations
- enqueue(): add an item to the end of the queue
- dequeue(): remove and return the item at the front

## Breadth-First Search Algorithm
- Uses Queue in the algorithm
- Also does not guarantee finding the shortest path
- Time Complexity: O(N*M) for N is number of rows and N is number of columns

Implementation
- bfs.py

## The Priority Queue Data Structure
- **Priority Queue** is a queue with precedence or priority for each item

Priority Queue Operations
- get(): retreive the item with the highest priority
- put(item): add item to priority queue
- is_empty(): determine if the priority queue is empty

Implementation
- priority_queue.py
- This implementation uses Python data structure: heapq
  - heapq holds list of tuples: [ ( priority, item),... ]
  - Only the first element will be the highest priority value. There is no guarantee of order of priority for other elements.
  
## A* Search Algorithm
- A* Search Algorithm uses **heuristic** to determine the likely best choice for each step of the algorithm
  - Heuristic: rule of thumb
  - In A* algorithm, heuristic is to choose the next position to visit based on its distance from the goal
- Distance is calculated using Manhattan distance
  - Manhattan Distance: distance between two points on a 2D grid when the path between those two points has to follow the grid layout
  - Distance between two points is measured along the axes at right angles
- Time Complexity: O(N*M) for N is number of rows and N is number of columns

Key Values in A* Algorithm
- G value: best distance from start to current cell
- H value: heuristic distance from the current cell to destination
- F value: the sum of the G value and the H value (representing the probable optimal value or minimum distance based on the heuristic used)

Implementation
- a_star.py


## Citation
These materials are from the Python Data Structures and Algorithms course in LinkedIn Learning by Robit Andrews, along with some research on Google.
