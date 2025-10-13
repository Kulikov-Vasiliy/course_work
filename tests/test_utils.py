import pytest

from src.utils import transactions


def test_transactions(transaction_data, summed, same):
    transaction_data = {
        "date": "21.12.2021",
        "amount": 1198.23,
        "category": "Переводы",
        "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    }
    result = transaction_data["amount"] += same["Сумма операции"]
    assert result == summed

    """if ("date" in transaction_data
                and "category" in transaction_data
                and "description" in transaction_data):
                transaction_data["amount"] += sorted_df["Сумма операции"] """

"""                transaction_data[row["Сумма операции"]] = {
                    "date": row["Дата платежа"],
                    "amount": row["Сумма операции"],
                    "category": row["Категория"],
                    "description": row["Описание"]"""

# @patch("requests.get")
# def test_currency_to_rubs_if_4xx(mock_get, operations_filled):
#     # Настраиваем mock на возврат ошибки HTTP 429
#     mock_response = Mock()
#     mock_response.status_code = 450
#     mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
#         "450 Client Error"
#     )
#     mock_response.json.return_value = {}
#     mock_get.return_value = mock_response
#
#     for operation in operations_filled:
#         currency_code = operation["operationAmount"]["currency"]["code"]
#         if currency_code != "RUB":
#             result = currency_to_rubs(operation)
#             assert result == "Client Error: 450"
#
#
# @patch("requests.get")
# def test_currency_to_rubs_if_5xx(mock_get, operations_filled):
#     mock_response = Mock()
#     mock_response.status_code = 504
#     mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
#         "504 Server Error"
#     )
#     mock_response.json.return_value = {}
#     mock_get.return_value = mock_response
#
#     for operation in operations_filled:
#         currency_code = operation["operationAmount"]["currency"]["code"]
#         if currency_code != "RUB":
#             result = currency_to_rubs(operation)
#             assert result == "Server Error"