##################################
#Talhakhan552 (GITHUB)

##################################

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        newNode = Node(item)
        if self.head is None:  
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def removeFromEnd(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data


    def removeFromFront(self):
        if not self.head:
            return None
        head_data = self.head.data
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return head_data




class Stack:
    def __init__(self):
        self.list = DoublyLinkedList()
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        return self.list.removeFromEnd()
    
    def isEmpty(self):
        return self.list.head is None



class Queue:
    def __init__(self):
        self.list = DoublyLinkedList()
    
    def enqueue(self, value):
        self.list.append(value)
    
    def dequeue(self):
        return self.list.removeFromFront()
    
    def isEmpty(self):
        return self.list.head is None




#Stack
class MazeSOlverStack:
    def __init__(self, maze):
        self.maze = maze
        self.start = None
        self.goal = None
        self.visited = [[False for i in row] for row in maze]
        self.StartAndGoal()

    def StartAndGoal(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    self.start = (i, j)         
                elif self.maze[i][j] == 'G':
                    self.goal = (i, j)
                    
                    
                    
    def solveMaze(self):
        print("Maze 1")  

        stack = Stack()
        stack.push(self.start)

        while not stack.isEmpty():
            cur = stack.pop()
            row,col =cur  
            if self.visited[row][col]:
                continue

            self.visited[row][col] = True
            self.printMaze()

            if cur == self.goal:
                print("you reached end Yay!!!!")
                print("goal can be reached :)")
                return True

            directions = [(0, 1),(1, 0),(0, -1), (-1, 0)]  
            for r,c in reversed(directions):  
                newrow = row + r
                newcol = col + c
                if self.ValidMove(newrow, newcol):
                    stack.push((newrow, newcol))

        print("goal cannot be reached :(")
        return False

    def ValidMove(self,row,col):
        if not (0 <= row < len(self.maze) and 0 <= col < len(self.maze[0])):
            return False  
        if self.maze[row][col] in ('.', 'G') and not self.visited[row][col]:
            return True
        
        return False


    def printMaze(self):
        for i in range(len(self.maze)):
            line = ''
            for j in range(len(self.maze[i])):
                if self.visited[i][j]:
                    line += 'e'  
                else:
                    line += self.maze[i][j]
            print(line)
        print("-------")
        
        

def readMazeFilestack(file):
    with open(file,'r')as file:
        data = file.readlines()

        dimen = data[1].strip().split()
        r = int(dimen[0])  
        c = int(dimen[1])
        
        maze = []
        for i in range(2, 2 + r):
            mazeRow= list(data[i].strip())  
            maze.append(mazeRow)  
    return maze  




#stack Driver mazw
filepath = input("Enter path of maze.txt: ")  
mazefile = readMazeFilestack(filepath)  
stacksolve = MazeSOlverStack(mazefile)
stacksolve.solveMaze()







#Queue
class MazeSolverQueue:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = None
        self.goal = None
        self.visited = [[False for i in range(self.cols)] for i in range(self.rows)]
        self.StartAndGoal()  

    def StartAndGoal(self):
        for i in range(len(self.maze)):      
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    self.start = (i, j)           
                elif self.maze[i][j] == 'G':
                    self.goal = (i, j)

    def ValidMove(self,row,col):
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return False  
        if self.maze[row][col] in ('.', 'G') and not self.visited[row][col]:
            return True
        
        return False



    #bonus
    def solveMazebonus(self):
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        if not self.start or not self.goal:
            print("Start or goal not found")
            return

        queue = [(self.start, [self.start])]  
        total_paths = 0
        shortest_path = None

        while queue:
            (cur_row, cur_col), path = queue.pop(0)  

            if self.visited[cur_row][cur_col]:
                continue
            
            self.visited[cur_row][cur_col] = True

            if (cur_row, cur_col) == self.goal:
                total_paths += 1
                if shortest_path is None or len(path) < len(shortest_path):
                    shortest_path = path
                continue

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for r,c in directions:
                newrow = cur_row + r
                newcol = cur_col + c
                if self.ValidMove(newrow, newcol):
                    queue.append(((newrow, newcol), path + [(newrow, newcol)]))

        if shortest_path:
            print(f"Shortest Path: {shortest_path}")
            print(f"Number of Paths: {total_paths}")
            self.printMazeforB(shortest_path)
        else:
            print("No valid path from starrt")




    def solveMaze(self):
        print("Maze 1")

        queue = Queue()
        queue.enqueue(self.start)

        while not queue.isEmpty():
            cur =queue.dequeue()
            row,col = cur
            if self.visited[row][col]:
                continue

            self.visited[row][col] = True
            #queue me row col diya
            self.printMaze(row,col)

            if cur == self.goal:
                print("you reached end Yay!!!!")
                print("goal can be reached :)")
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for r,c in directions:
                newrow = row + r
                newcol = col + c
                if self.ValidMove(newrow, newcol):
                    queue.enqueue((newrow, newcol))

        print("goal cannot be reached :(")
        return False




    
    
    def printMaze(self,row,col):
        for i in range(len(self.maze)):
            line = ''
            for j in range(len(self.maze[i])):
                if self.visited[i][j]:
                    line +='e'
                else:
                    line += self.maze[i][j]
            print(line)
            
            
        #row col print karwanay
        print(f"{row} {col}")  
        print("------")



    #bonus print
    def printMazeforB(self, path):
        maze_copy = [list(row) for row in self.maze]
        for (x, y) in path:
            if maze_copy[x][y] not in ('S','G'):
                maze_copy[x][y] = 'e'
        for row in maze_copy:
            print("".join(row))
        print("------")



def readMazeFile(file_path):
    with open(file_path,'r')as file:
        data = file.readlines()

        dimen = data[1].split()
        r = int(dimen[0])
        c = int(dimen[1])

        maze = []
        for i in range(2, 2 + r):
            mazeRow= list(data[i].strip())  
            maze.append(mazeRow)  
    return maze  


#qeueu Driver 
filepath = input("Enter path of maze.txt: ")  
mazefile = readMazeFile(filepath) 
queuesolver = MazeSolverQueue(mazefile)
queuesolver.solveMaze()


#Bonus Driver
mazefile = readMazeFile(filepath)
queuesolver.solveMazebonus()


























