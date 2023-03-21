import requests
api = 'http://localhost:7000'
def test_health():
    response =requests.get(f'{api}/health')
    assert response.status_code == 200
