def test_home_page(client):
    """Test that home page loads and contains expected h1"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Hello, world!</h1>' in response.data

def test_blinker_page(client):
    """Test that blinker example page loads"""
    size = 8  # Chess board size
    response = client.get('/examples/blinker')
    assert response.status_code == 200
    assert response.data.count(b'<td>') == size * size, f"Expecting a {size}x{size} table"
