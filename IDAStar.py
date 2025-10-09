from grid import grid
from sys import maxsize as maxInt
def IDAStar_Search(grid, start, goal,threshold=10):
    path=[start]
    while True:
        temp = Search(grid, start, 0, threshold, goal,path)
        if temp == 0:
            return path #TODO cambiar esto a que te devuelva el camino 
        if temp == maxInt:
            return False #No hay camino
        threshold = temp

def Search(grid, node, g, threshold, goal,path, parent=None):
    f = g + manh_dist(node,goal)
    if f > threshold:
        return f
    if grid[node[0]][node[1]]==2: #Is the goal
        return 0

    min_exceed = maxInt

    for child in expand(node,grid):
        if child==parent:
            continue
        path.append(child)
        #SE QUEDA ATRANCADO EN EL 2,3 --> 2,2 --> 2,3 -->2,2
        temp = Search(grid,child, g + 1, threshold,goal,path,node)
        if temp == 0:
            return 0
        if temp < min_exceed:
            min_exceed = temp
        path.pop()  # backtrack

    return min_exceed

def expand(node,grid):
    children=[]
    if node[0]>0:
        if grid[node[0]-1][node[1]] in (0,2) :
            children.append((node[0]-1,node[1]))
    
    if node[0]<len(grid)-1:
        if grid[(node[0]+1)][node[1]] in (0,2):
            children.append((node[0]+1,node[1]))
    
    if node[1]>0:
        if grid[node[0]][node[1]-1] in (0,2):
            children.append((node[0],node[1]-1))
    
    if node[1]<len(grid[node[0]])-1:
        if grid[node[0]][node[1]+1] in (0,2):
            children.append((node[0],node[1]+1))

    return children

def manh_dist(node,goal):
    return abs(node[0]-goal[0])+abs(node[1]-goal[1])

#IDAStar_Search(grid,(0,0),(3,4))
print(IDAStar_Search(grid,(0,0),(3,4)))