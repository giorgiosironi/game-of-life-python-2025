from world import AliveCell, WorldState

def count_alive_neighbors(world_state: WorldState, cell: AliveCell) -> int:
    pass

def evolve(world_state: WorldState) -> WorldState:
    for cell in world_state:
        alive_neighbors = count_alive_neighbors(world_state, cell)
    return []
