from neighborhood import count_alive_neighbors
from world import WorldState

def evolve(world_state: WorldState) -> WorldState:
    for cell in world_state:
        alive_neighbors = count_alive_neighbors(world_state, cell)
    return []
