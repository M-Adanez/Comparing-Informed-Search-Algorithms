
from grid import grid
import numpy as np
import heapq
import itertools

class Node:
    def __init__(self, state=(0, 0), path_cost=0, parent=None):
        self.state = state
        self.path_cost = path_cost
        self.parent = parent
        
    def __repr__(self):
        return str(self.state)

def f(node, goal, w):
    """Weighted A* cost estimation."""
    return  node.path_cost + w * h(node, goal)

def h(node, goal):
    """Manhattan distance function."""
    return np.abs(goal.state[0] - node.state[0]) + \
        np.abs(goal.state[1] - node.state[1])

def apply_move(node, move):
    """Returns a new node applying the given move."""
    new_x = node.state[0] + move[0]
    new_y = node.state[1] + move[1]
    return Node(state=(new_x, new_y), path_cost=node.path_cost + 1, parent=node)

def is_legal(node):
    """Checks if a move is valid."""
    if (node.state[0] < 0 or node.state[0] >= len(grid[0])) or \
        (node.state[1] < 0 or node.state[1] >= len(grid)) or \
            grid[node.state[1]][node.state[0]] == 1:
        return False
    return True

def expand(grid, node):
    """Searches for adjacent nodes."""
    neighs = []
    moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    for move in moves:
        new_node = apply_move(node, move)
        if is_legal(new_node):
            neighs.append(new_node)
    
    return neighs


def solution(node):
    """Given a node, reconstructs the path."""
    path = []
    curr = node
    while curr is not None:
        path.append(curr)
        curr = curr.parent
    return list(reversed(path))

def weighted_a_star(grid, init, goal, w):
    """Performs WA* search."""
    counter = itertools.count() # tiebreaker
    node = init
    frontier = []
    heapq.heappush(frontier, (f(node, goal, w), next(counter), node))
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)[2]
        if node.state == goal.state:
            return solution(node)
        
        explored.add(node)
        for child in expand(grid, node):
            if child not in explored:
                heapq.heappush(frontier, (f(child, goal, w), next(counter), child))
    return None


def main():
    init = Node(state=(0, 0), path_cost=0)
    goal = Node(state=(9, 9))
    w = 1.5

    path = weighted_a_star(grid, init, goal, w)
    if path:
        print(path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
