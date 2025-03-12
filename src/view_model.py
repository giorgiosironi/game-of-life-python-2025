def construct_view_model(alive_cells, max_x, max_y):
    return [_construct_row(max_x) for y in range(max_y+1)]

def _construct_row(max_x):
    return [False for _ in range(max_x + 1)]
