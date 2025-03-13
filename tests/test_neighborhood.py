from neighborhood import find_neighbors
from world import AliveCell


def test_find_neighbors_returns_eight_neighbors():
    # Arrange
    cell = AliveCell(x=4, y=7)  # Arbitrary position
    
    # Act
    neighbors = find_neighbors(cell)
    
    # Assert
    assert len(neighbors) == 8
