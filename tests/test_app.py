from bs4 import BeautifulSoup, Tag

from fixtures_types import LoadPage

default_width, default_height = 8, 6


def assert_table_has_custom_dimensions(soup: BeautifulSoup, custom_width: int, custom_height: int) -> None:
    """Checks for specific table dimensions"""
    assert len(soup.select('td')) == custom_width * \
        custom_height, f"Expecting a {custom_width}x{custom_height} table"


def assert_table_is_displayed(soup: BeautifulSoup) -> None:
    """Checks consistent and correct dimensions"""
    assert_table_has_custom_dimensions(soup, default_width, default_height)


def assert_only_a_blinker_is_present(soup: BeautifulSoup) -> None:
    """Smoke tests that only 3 living cells are displayed"""
    assert len(soup.select('td.cell--alive')
               ) == 3, "Expecting exactly 3 living cells"


def _single_attribute(tag: Tag, attribute_name: str) -> str:
    """Ensure a BeautifulSoup data attribute is a string."""
    attr = tag.get(attribute_name)
    assert isinstance(attr, str), "Expected data attribute to be a string"
    return attr


def assert_blinker_is_horizontal(soup: BeautifulSoup) -> None:
    """Checks that all living cells share the same y coordinate"""
    alive_y_coords = [int(_single_attribute(cell, 'data-y'))
                      for cell in soup.select('td.cell--alive')]
    assert len(set(alive_y_coords)
               ) == 1, "Expecting all cells to share the same y coordinate"


def assert_blinker_is_vertical(soup: BeautifulSoup) -> None:
    """Checks that all living cells share the same x coordinate"""
    alive_x_coords = [int(_single_attribute(cell, 'data-x'))
                      for cell in soup.select('td.cell--alive')]
    assert len(set(alive_x_coords)
               ) == 1, "Expecting all cells to share the same x coordinate"


def test_home_page_loads(load_page: LoadPage) -> None:
    soup = load_page('/')
    h1 = soup.select_one('h1')
    assert h1 is not None
    assert h1.text == 'Hello, world!'


def test_blinker_starts_horizontal(load_page: LoadPage) -> None:
    soup = load_page('/examples/blinker')
    assert_table_is_displayed(soup)
    assert_only_a_blinker_is_present(soup)
    assert_blinker_is_horizontal(soup)


def test_blinker_evolves_to_vertical(load_page: LoadPage) -> None:
    soup = load_page('/examples/blinker?generation=2')
    assert_table_is_displayed(soup)
    assert_only_a_blinker_is_present(soup)
    assert_blinker_is_vertical(soup)


def test_blinker_cycles_back_to_horizontal_in_any_odd_generation(load_page: LoadPage) -> None:
    soup = load_page('/examples/blinker?generation=3')
    assert_table_is_displayed(soup)
    assert_only_a_blinker_is_present(soup)
    assert_blinker_is_horizontal(soup)


def test_blinker_cycles_back_to_vertical_in_any_even_generation(load_page: LoadPage) -> None:
    soup = load_page('/examples/blinker?generation=4')
    assert_table_is_displayed(soup)
    assert_only_a_blinker_is_present(soup)
    assert_blinker_is_vertical(soup)


def test_the_world_window_can_have_custom_dimensions(load_page: LoadPage) -> None:
    custom_width, custom_height = 4, 3
    soup = load_page(
        f'/examples/blinker?width={custom_width}&height={custom_height}')
    assert_table_has_custom_dimensions(soup, custom_width, custom_height)
