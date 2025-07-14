# Maze-solver

A Python application designed to solve mazes using stacks and queues. The program solves the maze using a **Depth-First Search (DFS)** approach without recursion, and then expands the problem by using a **Breadth-First Search (BFS)** for a multi-agent solution. The maze solver finds a path from the start point ('S') to the goal point ('G') while handling obstacles (represented by `#`) and traversable paths (`.`).

## Features

- **DFS Approach (Part I)**  
  - Uses a **stack** to explore the maze from the starting point, backtracking when necessary.
  - Marks visited paths and explores all possible directions (East, South, West, North).
  - Solves the maze without recursion by using stack operations: Push, Pop, and Peek.

- **BFS Approach (Part II)**  
  - Simulates multiple agents working in parallel to find the goal more quickly using a **queue**.
  - Each agent explores the maze and tries different paths.
  - The first agent to reach the goal ends the search.
  
- **Shortest Path (Bonus)**  
  - Finds and prints the shortest path from the start to the finish.
  - Reports the number of possible paths from start to finish.

## How It Works

1. **Input (maze.txt)**  
   - The program reads a maze from a text file (`maze.txt`).  
   - The first line contains the dimensions of the maze (rows x columns).
   - The maze uses:
     - `S` for the start point.
     - `G` for the goal point.
     - `#` for obstacles.
     - `.` for open paths.
   
2. **Algorithm Overview (DFS)**  
   - Push the start position onto the stack.
   - While the stack is not empty:
     - Pop the stack to get the current location.
     - If the location is the goal (`G`), the maze is solved.
     - If the location has been visited, skip it.
     - Otherwise, explore adjacent positions (East, South, West, North) and push them onto the stack.
     - Mark locations as visited to avoid re-exploration.

3. **Algorithm Overview (BFS)**  
   - Each agent explores one possible direction at a time and fills out a queue for exploration.
   - Agents that reach the goal terminate the search.

4. **Output**  
   - The program will display the exploration progress and the final maze with the path marked (`e` for explored).
   - It reports whether the goal is reachable and the shortest path if applicable.

## Sample Input (`maze.txt`)

