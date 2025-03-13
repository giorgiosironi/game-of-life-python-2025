from dataclasses import dataclass
from typing import List, TypeAlias

@dataclass(frozen=True)
class AliveCell:
    x: int
    y: int 

WorldState: TypeAlias = List[AliveCell]
