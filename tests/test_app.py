from bs4 import BeautifulSoup

def test_home_page(page):
    """Test that home page loads and contains expected h1"""
    soup = page('/')
    assert soup.select_one('h1').text == 'Hello, world!'

def test_blinker_page(page):
    """Test that blinker example page loads"""
    width, height = 8, 6
    soup = page('/examples/blinker')
    assert len(soup.select('td')) == width * height, f"Expecting a {width}x{height} table"
    assert len(soup.select('td.cell--alive')) == 3, "Expecting exactly 3 living cells"

def test_blinker_evolves(page):
    """Test that blinker example page evolves to the next generation"""
    width, height = 8, 6
    soup = page('/examples/blinker?generation=2')
    assert len(soup.select('td')) == width * height, f"Expecting a {width}x{height} table"
    assert len(soup.select('td.cell--alive')) == 3, "Expecting exactly 3 living cells"
