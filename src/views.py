# функции генерации json-ответов
import json
import logging
from json import JSONDecodeError
import os

from src.utils import (
    get_card_spent,
    get_currency,
    get_date_time,
    get_path_period,
    get_stock_price,
    greet_result,
    transactions,
)

logger = logging.getLogger("views")
log = os.path.join(os.path.dirname(__file__),'..', 'logs', 'views.log')
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__),"../logs/views.log"),
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def greetings(date_time: str) -> str:
    """Приветствие пользователя в зависимости от его времени суток"""
    greeting = greet_result()
    time_period = get_date_time(date_time)
    sorted_df = get_path_period(
        os.path.join(os.path.dirname(__file__),"../data/operations.xlsx"),
        time_period,
    )
    cards = get_card_spent(sorted_df)
    top_transactions = transactions(sorted_df)
    currency_rates = get_currency()
    stock_prices = get_stock_price()
    try:
        logger.info("получение и формирование json-ответа")
        data = {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_transactions,
            "currency_rates": currency_rates,
            "stock_prices": stock_prices,
        }

        json_data = json.dumps(data, ensure_ascii=False, indent=4)

        logger.info("успешно сформирован ответ")
        return json_data

    except JSONDecodeError:
        logger.error("Произошла ошибка кодирования")
        return "ошибка формирования ответа"
