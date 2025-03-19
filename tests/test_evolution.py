from evolution import evolve
from world import AliveCell, WorldState


def test_empty_world_stays_empty() -> None:
    world_state: WorldState = []

    next_state = evolve(world_state)

    assert len(next_state) == 0, "Expected no cells to be alive in next generation"


def test_underpopulation_single_alive_cell_dies() -> None:
    world_state: WorldState = [AliveCell(x=1, y=1)]

    next_state = evolve(world_state)

    assert AliveCell(
        1, 1) not in next_state, "Expected cell at (1,1) to die from underpopulation"


def test_underpopulation_alive_cell_with_one_alive_neighbor_dies() -> None:
    world_state: WorldState = [
        AliveCell(x=1, y=1),
        AliveCell(x=1, y=2),
    ]

    next_state = evolve(world_state)

    assert AliveCell(
        1, 1) not in next_state, "Expected cell at (1,1) to die from underpopulation"


def test_survival_alive_cell_with_two_alive_neighbors_lives() -> None:
    world_state: WorldState = [
        AliveCell(x=1, y=1),
        AliveCell(x=1, y=2),
        AliveCell(x=1, y=0),
    ]

    next_state = evolve(world_state)

    assert AliveCell(
        1, 1) in next_state, "Expected cell at (1,1) to survive with two neighbors"


def test_cell_with_three_neighbors_survives() -> None:
    cell = AliveCell(x=1, y=1)
    neighbors = [
        AliveCell(x=0, y=0),
        AliveCell(x=0, y=1),
        AliveCell(x=0, y=2),
    ]
    world_state = [cell] + neighbors

    next_state = evolve(world_state)

    assert cell in next_state, "Expected cell with three neighbors should survive"


def test_overcrowding_alive_cell_with_four_neighbors_dies() -> None:
    cell = AliveCell(x=1, y=1)
    neighbors = [
        AliveCell(x=0, y=0),
        AliveCell(x=0, y=1),
        AliveCell(x=0, y=2),
        AliveCell(x=1, y=0),
    ]
    world_state = [cell] + neighbors

    next_state = evolve(world_state)

    assert cell not in next_state, "Expected cell with four neighbors to die from overcrowding"


def test_reproduction_dead_cell_with_three_neighbors_becomes_alive() -> None:
    world_state = [
        AliveCell(x=0, y=0),
        AliveCell(x=0, y=1),
        AliveCell(x=0, y=2),
    ]

    next_state = evolve(world_state)

    assert AliveCell(
        1, 1) in next_state, "Expected dead cell at (1,1) to become alive from reproduction"
