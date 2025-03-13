from world import WorldState, evolve
from alive_cell import AliveCell

def test_empty_world_stays_empty():
    world_state: WorldState = []
    
    next_state = evolve(world_state)
    
    assert len(next_state) == 0, "Expected no cells to be alive in next generation"

def test_single_cell_dies():
    world_state: WorldState = [AliveCell(x=1, y=1)]
    
    next_state = evolve(world_state)
    
    assert len(next_state) == 0, "Expected lonely cell to die in next generation" 
