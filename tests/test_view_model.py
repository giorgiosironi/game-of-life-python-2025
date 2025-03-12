from view_model import AliveCell, construct_view_model

max_x = 2
max_y = 2
total_rows = max_y + 1
total_columns = max_x + 1

def count_alive_cells(view_model):
    return sum(cell for row in view_model for cell in row)

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
    alive_cells = [AliveCell(1, 2)]
    view_model = construct_view_model(alive_cells, max_x=max_x, max_y=max_y)
    
    assert_rows(view_model)
    assert_columns(view_model)
    assert count_alive_cells(view_model) == 1, "Expect one cell to be alive"
