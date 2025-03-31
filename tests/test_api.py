import requests

def test_detect_api():
    url = \"http://localhost:8000/detect\"
    payload = {\"text\": \"Suspicious transaction: transfer  to offshore account\"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert \"risk_level\" in data
