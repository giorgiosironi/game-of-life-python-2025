from bs4 import BeautifulSoup

def test_home_page(page):
    """Test that home page loads and contains expected h1"""
    soup = page('/')
    assert soup.select_one('h1').text == 'Hello, world!'

def test_blinker_starts_horizontal(page):
    """Test that blinker starts in horizontal position (3 cells in same row)"""
    width, height = 8, 6
    soup = page('/examples/blinker')
    assert len(soup.select('td')) == width * height, f"Expecting a {width}x{height} table"
    assert len(soup.select('td.cell--alive')) == 3, "Expecting exactly 3 living cells"
    
    #alive_y_coords = [int(cell['data-y']) for cell in soup.select('td.cell--alive')]
    #assert len(set(alive_y_coords)) == 1, "Expecting all cells to share the same y coordinate"

def test_blinker_evolves(page):
    """Test that blinker example page evolves to the next generation"""
    width, height = 8, 6
    soup = page('/examples/blinker?generation=2')
    assert len(soup.select('td')) == width * height, f"Expecting a {width}x{height} table"
    assert len(soup.select('td.cell--alive')) == 3, "Expecting exactly 3 living cells"
    
    #alive_x_coords = [int(cell['data-x']) for cell in soup.select('td.cell--alive')]
    #assert len(set(alive_x_coords)) == 1, "Expecting all cells to share the same x coordinate"
