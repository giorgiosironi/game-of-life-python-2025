from neighborhood import find_neighbors
from world import AliveCell


def test_find_neighbors_returns_eight_neighbors() -> None:
    cell = AliveCell(x=4, y=7)  # Arbitrary position

    neighbors = find_neighbors(cell)

    assert len(neighbors) == 8
    for neighbor in neighbors:
        x_diff = abs(neighbor.x - cell.x)
        y_diff = abs(neighbor.y - cell.y)
        assert x_diff <= 1 and y_diff <= 1, f"Neighbor {neighbor} is too far from cell {cell}"
    assert cell not in neighbors, f"Cell {cell} cannot be a neighbor of itself"
    assert len(set(neighbors)) == 8, "Neighbors contains duplicates"
