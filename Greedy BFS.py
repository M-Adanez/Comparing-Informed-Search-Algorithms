from grid import grid
import heapq

def greedy_best_first_search(grid, init, objective):
    start=init
    goal = objective
    frontier = []
    cost=0
    heapq.heappush(frontier, (cost, start))
    explored = set()
    
    while(frontier):
        current = heapq.heappop(frontier)[1]
        if current == goal:
            return True
        explored.add(current)
        for neighbor in grid.get_neighbors(current):
            if neighbor not in explored:
                priority = grid.heuristic(neighbor, goal)
                cost+=1
                heapq.heappush(frontier, (priority, neighbor))

                
    return False
    

def get_neighbors():
    
    pass
