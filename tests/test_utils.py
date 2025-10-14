from unittest.mock import patch, Mock

import pytest

import requests

from src.utils import transactions, get_currency, get_stock_price


def test_transactions(summed, same):
    transaction_data = {
        "date": "21.12.2021",
        "amount": 1198.23,
        "category": "Переводы",
        "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    }
    if "date" in transaction_data and "category" in transaction_data and "description" in transaction_data:
        transaction_data["amount"] += same["Сумма операции"]
    assert transaction_data["amount"] == summed


@patch("requests.get")
def test_get_currency_if_4xx(mock_get):
    mock_response = Mock()
    mock_response.status_code = 450
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "Client Error: 450"
    )
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
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "Client Error: 450"
    )
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
