def test_home_page(client):
    """Test that home page loads and contains expected h1"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Hello, world!</h1>' in response.data
