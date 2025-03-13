from evolution import WorldState, evolve
from world import AliveCell

def test_empty_world_stays_empty():
    world_state: WorldState = []
    
    next_state = evolve(world_state)
    
    assert len(next_state) == 0, "Expected no cells to be alive in next generation"

def test_underpopulation_single_alive_cell_dies():
    world_state: WorldState = [AliveCell(x=1, y=1)]
    
    next_state = evolve(world_state)
    
    assert AliveCell(1, 1) not in next_state, "Expected cell at (1,1) to die from underpopulation"

def test_underpopulation_alive_cell_with_one_alive_neighbor_dies():
    world_state: WorldState = [
        AliveCell(x=1, y=1),
        AliveCell(x=1, y=2),
    ]
    
    next_state = evolve(world_state)
    
    assert AliveCell(1, 1) not in next_state, "Expected cell at (1,1) to die from underpopulation"

def test_survival_alive_cell_with_two_alive_neighbors_lives():
    world_state: WorldState = [
        AliveCell(x=1, y=1),
        AliveCell(x=1, y=2),
        AliveCell(x=1, y=0),
    ]
    
    next_state = evolve(world_state)
    
    assert AliveCell(1, 1) in next_state, "Expected cell at (1,1) to survive with two neighbors" 
