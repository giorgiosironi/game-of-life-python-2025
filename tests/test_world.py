from world import WorldState, evolve

def test_empty_world_stays_empty():
    world_state: WorldState = []
    
    next_state = evolve(world_state)
    
    assert len(next_state) == 0, "Expected no cells to be alive in next generation" 
