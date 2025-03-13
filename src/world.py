from typing import List, TypeAlias
from alive_cell import AliveCell

WorldState: TypeAlias = List[AliveCell]

def evolve(world_state: WorldState) -> WorldState:
    return world_state 
