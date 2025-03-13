from view_model import DisplayedCell, construct_view_model
from world import AliveCell

max_x = 2
max_y = 2
total_rows = max_y + 1
total_columns = max_x + 1

def count_alive_cells(view_model):
    return sum(cell.alive for row in view_model for cell in row)

def assert_rows(view_model):
    assert len(view_model) == total_rows, f"Expected {total_rows} rows"

def assert_columns(view_model):
    for row_index, row in enumerate(view_model):
        assert len(row) == total_columns, f"Expected {total_columns} cells in row {row_index}"

def test_empty_list_of_alive_cells_displays_all_dead_cells():
    alive_cells = []
    view_model = construct_view_model(alive_cells, max_x=max_x, max_y=max_y)
    
    assert_rows(view_model)
    assert_columns(view_model)
    assert count_alive_cells(view_model) == 0, "Expect all cells to be dead"

def test_one_alive_cell_is_displayed():
    x = 1
    y = 2
    alive_cells = [AliveCell(x, y)]
    view_model = construct_view_model(alive_cells, max_x=max_x, max_y=max_y)
    
    assert_rows(view_model)
    assert_columns(view_model)
    assert count_alive_cells(view_model) == 1, "Expect one cell to be alive"
    
    cell = view_model[y][x]
    assert cell.alive, "Expect the correct cell to be alive"
    assert cell.x == x, "Cell should have correct x coordinate"
    assert cell.y == y, "Cell should have correct y coordinate"

def test_two_alive_cells_are_displayed():
    x1, y1 = 0, 0  # top-left corner
    x2, y2 = 2, 2  # bottom-right corner
    alive_cells = [
        AliveCell(x1, y1),
        AliveCell(x2, y2),
    ]
    view_model = construct_view_model(alive_cells, max_x=max_x, max_y=max_y)
    
    assert_rows(view_model)
    assert_columns(view_model)
    assert count_alive_cells(view_model) == 2, "Expect two cells to be alive"
    
    cell1 = view_model[y1][x1]
    assert cell1.alive, "Expect top-left cell to be alive"
    assert cell1.x == x1, "Top-left cell should have correct x coordinate"
    assert cell1.y == y1, "Top-left cell should have correct y coordinate"
    
    cell2 = view_model[y2][x2]
    assert cell2.alive, "Expect bottom-right cell to be alive"
    assert cell2.x == x2, "Bottom-right cell should have correct x coordinate"
    assert cell2.y == y2, "Bottom-right cell should have correct y coordinate"
