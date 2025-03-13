from typing import List
from world import AliveCell, WorldState

def find_neighbors(cell: AliveCell) -> List[AliveCell]:
    return [cell for i in range(8)]
