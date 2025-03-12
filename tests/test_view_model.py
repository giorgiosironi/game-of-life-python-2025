from view_model import construct_view_model

def count_alive_cells(view_model):
    return sum(cell for row in view_model for cell in row)

def test_empty_list_of_alive_cells_displays_all_dead_cells():
    alive_cells = []
    view_model = construct_view_model(alive_cells, max_x=2, max_y=2)
    
    assert len(view_model) == 3, "Expected 3 rows"
    assert len(view_model[0]) == 3, "Expected 3 cells in the first row"
    assert count_alive_cells(view_model) == 0, "Expect all cells to be dead"

