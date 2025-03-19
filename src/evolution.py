from neighborhood import find_neighbors
from world import WorldState


def evolve(world_state: WorldState) -> WorldState:
    next_state = []
    considered_cells = set()

    for cell in world_state:
        considered_cells.add(cell)
        for neighbor in find_neighbors(cell):
            considered_cells.add(neighbor)

    for cell in considered_cells:
        neighbors = find_neighbors(cell)
        alive_neighbors = sum(
            1 for neighbor in neighbors if neighbor in world_state)
        if cell in world_state:
            if alive_neighbors in [2, 3]:
                next_state.append(cell)
        else:
            if alive_neighbors == 3:
                next_state.append(cell)
    return next_state
