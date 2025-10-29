from unittest.mock import patch, Mock


import requests

from src.utils import get_currency, get_stock_price


@patch("requests.get")
def test_get_currency_if_4xx(mock_get):
    mock_response = Mock()
    mock_response.status_code = 450
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Client Error: 450")
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response
    result = get_currency()
    assert result == "Client Error: 450"


@patch("requests.get")
def test_get_currency_if_5xx(mock_get):
    mock_response = Mock()
    mock_response.status_code = 504
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Server Error")
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response
    result = get_currency()
    assert result == "Server Error"


@patch("requests.get")
def test_get_stock_price_if_4xx(mock_get):
    mock_response = Mock()
    mock_response.status_code = 450
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Client Error: 450")
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response
    result = get_stock_price()
    assert result == "Client Error: 450"


@patch("requests.get")
def test_get_stock_price_if_5xx(mock_get):
    mock_response = Mock()
    mock_response.status_code = 504
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Server Error")
    mock_response.json.return_value = {}
    mock_get.return_value = mock_response
    result = get_stock_price()
    assert result == "Server Error"
