import pytest
import requests

def test_app_running():
    url = "http://192.168.29.114:5001/" #"http://localhost:5001/"

    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200

    except requests.exceptions.RequestException as e:
        pytest.fail(f"App at the given {url} is not available. Error: {e}")