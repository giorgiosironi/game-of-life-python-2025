from dataclasses import dataclass
from world import AliveCell

@dataclass
class DisplayedCell:
    x: int
    y: int
    alive: bool

def construct_view_model(alive_cells, max_x, max_y):
    return [_construct_row(alive_cells, max_x + 1, y) for y in range(max_y+1)]

def _construct_row(alive_cells, row_length, y):
    return [DisplayedCell(x=x, y=y, alive=_is_cell_alive(alive_cells, x, y)) 
            for x in range(row_length)]

def _is_cell_alive(alive_cells, x, y):
    return AliveCell(x, y) in alive_cells
