
from grid import grid
import numpy as np
import heapq

class Node:
    def __init__(self, state=(0, 0), path_cost=0, parent=None):
        self.state = state
        self.path_cost = path_cost
        self.parent = parent

def f(node, goal, w):
    """Weighted A* cost estimation."""
    return  node.path_cost + w * heuristic(node, goal)

def heuristic(node, goal):
    """Manhattan distance function."""
    return np.abs(goal.state[0] - node.state[0]) + \
        np.abs(goal.state[1] - node.state[1])

def expand(grid, node):
    neighs = []
    moves = []
    for i in range(2):
        for j in range(2):
            moves.append((i, j))

    for x, y in moves:
        if grid[y][x] != 1:
            neighs.append((node.state[0] + y, node.state[1] + x))
    
    return neighs


def solution(node):
    """Reconstructs the path given a node."""
    path = []
    curr = node
    while curr is not None:
        path.append(curr)
        curr = curr.parent
    return list(reversed(path))

def weighted_a_star(grid, init, goal, w):
    node = init
    frontier = heapq()
    entry_finder = {} # map of states and f() values
    heapq.heappush(init, f(node, goal, w))
    explored = set()

    while frontier:
        node = heapq.heappop()
        if node.state == goal.state:
            return solution(node)
        
        explored.add(node)
        for child in expand(grid, node):
            if child not in explored:
                heapq.heappush(frontier, f(child, goal, w))
            # TODO: revisar esta condicion
    return None



