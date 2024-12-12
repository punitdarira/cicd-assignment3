import azure.functions as func
from unittest.mock import Mock
from function_app import main  # Import the function directly

def test_main():
    # Create a mock HTTP request
    req = Mock(spec=func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={})

    # Call the function directly
    response = main(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello World from Punit Darira"

def test_main_with_params():
    # Create a mock HTTP request with parameters
    req = Mock(spec=func.HttpRequest)
    req.params = {'name': 'Punit'}
    req.get_json = Mock(return_value={})

    # Call the function directly
    response = main(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello World from Punit Darira"

def test_main_with_json():
    # Create a mock HTTP request with JSON body
    req = Mock(spec=func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={'name': 'Darira'})

    # Call the function directly
    response = main(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello World from Punit Darira"