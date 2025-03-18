from dataclasses import dataclass
from world import AliveCell, WorldState
from typing import List

@dataclass
class DisplayedCell:
    x: int
    y: int
    alive: bool

def construct_view_model(world_state: WorldState, max_x: int, max_y: int) -> List[List[DisplayedCell]]:
    return [_construct_row(world_state, max_x + 1, y) for y in range(max_y+1)]

def _construct_row(world_state: WorldState, row_length: int, y: int) -> List[DisplayedCell]:
    return [DisplayedCell(x=x, y=y, alive=_is_cell_alive(world_state, x, y)) 
            for x in range(row_length)]

def _is_cell_alive(world_state: WorldState, x: int, y: int) -> bool:
    return AliveCell(x, y) in world_state
