from neighborhood import find_neighbors
from world import WorldState

def evolve(world_state: WorldState) -> WorldState:
    next_state = []
    for cell in world_state:
        neighbors = find_neighbors(cell)
        alive_neighbors = sum(1 for neighbor in neighbors if neighbor in world_state)
        if alive_neighbors == 2:
            next_state.append(cell)
    return next_state
