from typing import List
from world import AliveCell


def find_neighbors(cell: AliveCell) -> List[AliveCell]:
    neighbors = [
        AliveCell(cell.x + dx, cell.y + dy)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if not (dx == 0 and dy == 0)  # Skip the cell itself
    ]
    return neighbors
