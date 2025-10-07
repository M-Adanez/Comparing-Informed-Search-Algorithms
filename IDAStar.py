from grid import grid
from sys import maxsize as maxInt
print(grid)

def IDAStar_Search(grid, start, goal,threshold=10):
    while True:
        temp = Search(grid, start, 0, threshold, goal)
        if temp == 0:
            return True #TODO cambiar esto a que te devuelva el camino 
        if temp == maxInt:
            return False #No hay camino
        threshold = temp

def Search(grid, node, g, threshold, goal):
    f = g + manh_dist(node,goal)
    if f > threshold:
        return f
    if grid[node[0]][node[1]]==2: #Is the goal
        return 0
    
    min_exceed = maxInt
    for child in expand(node, grid):
        temp = Search(grid,child, g + 1, threshold,goal)
        if temp == 0:
            return 0
        if temp < min_exceed:
            min_exceed = temp
    return min_exceed

def expand(node,grid):
    children=[]
    # NO PUEDES CALCULARLO DENTRO DE LA FUNCION PORQUE NO ENTRAN SI SON ILEGALES YA
    if is_legal((node[0]+1,node[1]),grid):
        children.append((node[0]+1,node[1]))
    if is_legal((node[0],node[1]+1),grid):
        children.append((node[0],node[1]+1))
    if is_legal((node[0]-1,node[1]),grid):
        children.append((node[0]-1,node[1]))
    if is_legal((node[0],node[1]-1),grid):
        children.append((node[0],node[1]-1))

    return children

def is_legal(node,grid):
    if node[0]<0:
        return False
    if node[0]>len(grid):
        return False
    if node[1]<0:
        return False
    if node[1]>len(grid[0]):
        return False
    
    if grid[node[0]][node[1]]==1:
        return False
    
    return True

def manh_dist(node,goal):
    return abs(node[0]-goal[0])+abs(node[1]-goal[1])

print(IDAStar_Search(grid,(0,0),(3,4),10))