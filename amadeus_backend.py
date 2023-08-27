import requests

base_url = "https://flights-api.buraky.workers.dev/"

def test_http_status_code():
    response = requests.get(base_url)
    assert response.status_code == 200, "API should return a 200 status code"

def test_response_content():
    response = requests.get(base_url)
    data = response.json()
    
    assert isinstance(data, dict), "Response content should be a dictionary"
    assert "data" in data, "Response should contain 'data' field"
    assert isinstance(data["data"], list), "'data' field should contain a list"
    for flight in data["data"]:
        assert all(key in flight for key in ["id", "from", "to", "date"]), "Each flight should contain 'id', 'from', 'to', and 'date' fields"

def test_response_headers():
    response = requests.get(base_url)
    headers = response.headers
    
    assert "Content-Type" in headers, "Response should contain 'Content-Type' header"
    assert headers["Content-Type"] == "application/json", "'Content-Type' header should be 'application/json'"

if __name__ == "__main__":
    test_http_status_code()
    test_response_content()
    test_response_headers()
    print("All backend tests passed successfully!")
