from neighborhood import find_neighbors
from world import WorldState

def evolve(world_state: WorldState) -> WorldState:
    for cell in world_state:
        neighbors = find_neighbors(cell)
        alive_neighbors = sum(1 for neighbor in neighbors if neighbor in world_state)
    return []
