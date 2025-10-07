from grid import grid
import heapq
print(grid)

def greedy_best_first_search(grid):
    cola_prioridad = []
    costo_inicial = 0
    fila_inicial = 0
    columna_inicial = 0
    frontier=heapq.heappush(cola_prioridad, (costo_inicial, fila_inicial, columna_inicial))
    
    while(frontier):
        if(fila_inicial==5 and columna_inicial==5):
            return "Solution found"
        elif(fila_inicial==0 and columna_inicial==0):
            
        

            pass

