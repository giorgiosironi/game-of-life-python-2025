from view_model import construct_view_model

max_x = 2
max_y = 2
total_rows = max_y + 1
total_columns = max_x + 1

def count_alive_cells(view_model):
    return sum(cell for row in view_model for cell in row)

def test_empty_list_of_alive_cells_displays_all_dead_cells():
    alive_cells = []
    view_model = construct_view_model(alive_cells, max_x=max_x, max_y=max_y)
    
    assert len(view_model) == total_rows, f"Expected {total_rows} rows"
    for row_index, row in enumerate(view_model):
        assert len(row) == total_columns, f"Expected {total_columns} cells in row {row_index}"
    assert count_alive_cells(view_model) == 0, "Expect all cells to be dead"

