from grid import grid
import heapq

def greedy_best_first_search(grid, init, objective):
    came_from = {init: None}
    frontier = []

    start_h = grid.heuristic(init, objective)
    heapq.heappush(frontier, (start_h, init))

    while frontier:
        current_h, current_node = heapq.heappop(frontier)

        if current_node == objective:
            return reconstruct_path(came_from, init, objective)
        for neighbor in grid.get_neighbors(current_node):
            if neighbor not in came_from:
                priority = grid.heuristic(neighbor, objective)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None and goal != start:
            return None 
            
    path.append(start)
    path.reverse() 
    return path

