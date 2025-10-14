# вспомогательные функции основного функционала
import os
from datetime import datetime

# noinspection PyUnresolvedReferences
import pandas as pd
import requests

# noinspection PyUnresolvedReferences
from dotenv import load_dotenv

# noinspection PyUnresolvedReferences
from pandas import DataFrame

from src.log_config import logger

load_dotenv()
CURRENCY_API = os.getenv("API_KEY_CURRENCY")
FOUNDATION_API = os.getenv("API_KEY_S&P500")
apiKey = os.getenv("API_KEY_RATE")


def greet_result() -> str:
    """Приветствие в формате «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи»"""
    logger.info(
        "получение даты и времени пользователя, ее настройка для получения времени"
    )
    now = datetime.now()
    time_form = now.strftime("%H:%M:%S")  # только время

    logger.info("определение сообщения приветствия")
    if "07:00:00" <= time_form <= "10:00:00":
        greet = "ое утро"
    elif "10:00:01" <= time_form <= "16:00:00":
        greet = "ый день"
    elif "16:00:01" <= time_form <= "22:00:00":
        greet = "ый вечер"
    else:
        greet = "ой ночи"

    return f"Добр{greet}"


def get_date_time(date_time: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> list[str]:
    """Меняет формат строки и фильтрует от начала месяца до указанного числа"""
    logger.info("настройка интервала дат от 1 числа месяца до указанного")
    dt = datetime.strptime(date_time, date_format)
    month_start = dt.replace(day=1)

    return [month_start.strftime("%d.%m.%Y %H:%M:%S"), dt.strftime("%d.%m.%Y %H:%M:%S")]


def get_path_period(path_file: str, time_period: list) -> DataFrame:
    """фильтрует отчет по интервалу дат"""
    logger.info("выбор нужной страницы excel-файла, ее сортировка")
    df = pd.read_excel(path_file, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    start_period = datetime.strptime(time_period[0], "%d.%m.%Y %H:%M:%S")
    last_date = datetime.strptime(time_period[1], "%d.%m.%Y %H:%M:%S")
    filtered_df = df[
        (df["Дата операции"] >= start_period) & (df["Дата операции"] <= last_date)
    ]
    sorted_df = filtered_df.sort_values(by="Дата операции", ascending=True)

    return sorted_df


def get_card_spent(sorted_df: DataFrame) -> list[dict]:
    """формирует из df список формата "cards":
    [{"last_digits": "5814",
      "total_spent": 1262.00,
      "cashback": 12.62}]"""
    cards = []
    card_spent = {}
    card_sorted = sorted_df[
        ["Номер карты", "Сумма операции", "Кэшбэк", "Сумма операции с округлением"]
    ]

    logger.info("отбор нужных данных для пар ключ-значение списка cards")
    for i, row in card_sorted.iterrows():
        sorted_df["Сумма операции"] = pd.to_numeric(
            sorted_df["Сумма операции"], errors="coerce"
        )
        sorted_df["Сумма операции с округлением"] = pd.to_numeric(
            sorted_df["Сумма операции с округлением"], errors="coerce"
        )
        sorted_df["Кэшбэк"] = pd.to_numeric(sorted_df["Кэшбэк"], errors="coerce")

        logger.info("проверка наличия номера карты в операции")
        if pd.isna(row["Номер карты"]):
            continue

        logger.info("создание пар ключ-значение по номеру карты")
        last_digit = str(row["Номер карты"]).strip()

        if last_digit not in card_spent:
            card_spent[last_digit] = {"total_spent": 0, "cashback": 0}

        logger.info("определение источника положительного значения сумм расходов")
        if row["Сумма операции"] < 0:
            total_spent = row["Сумма операции с округлением"]
        else:
            total_spent = row["Сумма операции"]

        logger.info("получение суммы возврата дс от расхода, вычисление сумм")
        cashback = (
            (row["Сумма операции"] / 100) if pd.isna(row["Кэшбэк"]) else row["Кэшбэк"]
        )
        cashback = abs(cashback)

        card_spent[last_digit]["total_spent"] += total_spent
        card_spent[last_digit]["cashback"] += cashback

    logger.info("формирование итоговых данных по картам и тратам")
    for card, values in card_spent.items():
        card_info = {
            "last_digits": card,
            "total_spent": round(values["total_spent"], 2),
            "cashback": round(values["cashback"], 2),
        }
        cards.append(card_info)

    return cards


def transactions(sorted_df: DataFrame) -> list[dict]:
    """формирует из df список формата "top_transactions":
    [{"date": "21.12.2021",
      "amount": 1198.23,
      "category": "Переводы",
      "description": "Перевод Кредитная карта. ТП 10.2 RUR"}]"""
    top_transactions = []
    transaction_data = {}
    transaction_sorted = sorted_df[
        ["Дата платежа", "Сумма операции", "Категория", "Описание"]
    ].sort_values(by="Дата платежа", ascending=False)

    logger.info(
        "определение источника данных для пар ключ-значение списка топ 5 расходов"
    )
    for date, group in transaction_sorted.groupby("Дата платежа"):
        top_5 = group.nlargest(5, "Сумма операции")
        for i, row in top_5.iterrows():
            logger.info("проверка наличия нужных данных")
            if pd.isna(
                row["Сумма операции"]
                or row["Категория"]
                or row["Описание"]
                or row["Дата платежа"]
            ):
                continue
            logger.info("подбор значений, суммирование одинаковых операций по карте")
            if "Сумма операции" not in transaction_data:
                transaction_data[row["Сумма операции"]] = {
                    "date": row["Дата платежа"],
                    "amount": row["Сумма операции"],
                    "category": row["Категория"],
                    "description": row["Описание"],
                }

            elif (
                "date" in transaction_data
                and "category" in transaction_data
                and "description" in transaction_data
            ):
                transaction_data["amount"] += sorted_df["Сумма операции"]  # type: ignore[assignment]

    logger.info("формирование итогового списка")
    for amount, values in transaction_data.items():
        data = {
            "date": values["date"],
            "amount": round(values["amount"], 2),
            "category": values["category"],
            "description": values["description"],
        }
        top_transactions.append(data)
        if len(top_transactions) >= 5:
            break

    return top_transactions


def get_currency() -> list[dict] | str:  # type: ignore[return]
    """получает стоимость USD и EUR и формирует список
    [{"currency": "USD",
    "rate": 82.00
    }]"""
    response = None
    currency_rate = []
    currencies = ["CNY", "EUR"]
    url = "https://www.alphavantage.co/query"

    for currency in currencies:
        payload = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": currency,
            "to_currency": "RUB",
            "apikey": CURRENCY_API,
        }

        try:
            logger.info("подключение к валютному api-ресурсу")
            response = requests.get(url, params=payload)
            response.raise_for_status()
            result = response.json()
            logger.info("получение стоимости валюты")
            if "Realtime Currency Exchange Rate" in result:
                rate = float(
                    result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
                )
                logger.info("формирование итога")
                data = {"currency": currency, "rate": round(rate, 2)}
                currency_rate.append(data)

            logger.info("итог успешно сформирован")
            return currency_rate

        except requests.exceptions.HTTPError:
            if 500 <= response.status_code < 600:  # type: ignore[union-attr]
                logger.error("Произошла ошибка сервера")
                return "Server Error"
            elif 400 <= response.status_code < 500:  # type: ignore[union-attr]
                logger.error(f"Произошла клиентская ошибка {response.status_code}")  # type: ignore[union-attr]
                return f"Client Error: {response.status_code}"  # type: ignore[union-attr]


def get_stock_price() -> list[dict] | str:  # type: ignore[return]
    """получает список с ценами ценных бумаг в составе фонда ОША и формирует список
    [{"stock": "AAPL",
     "price": 150.12}]"""
    response = None
    activ_rate = []
    try:
        api_url = "https://api.api-ninjas.com/v1/sp500"
        headers = {"X-Api-Key": FOUNDATION_API}
        logger.info(
            "подключение к api-ресурсу для получения актуального состава S&P500"
        )
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        result = response.json()
        logger.info("получение состава индекса")
        for el in result:
            ticker = el["ticker"]
            sector = el["sector"]
            company_name = el["company_name"]
            data = {
                "stock": ticker,
                "company_name": company_name,
                "sector": sector,
            }

            logger.info(
                "подключение к инвестиционному api-ресурсу для получения цены актива из состава индекса"
            )
            if "stock" in data:
                url = "https://finnhub.io/api/v1/quote"
                payload = {"token": apiKey, "symbol": ticker}
                response = requests.get(url, params=payload)
                response.raise_for_status()
                result = response.json()
                logger.info("формирование данных")
                data_rates = {
                    "price": round(result["c"], 2),
                    "High price of the day": round(result["h"], 2),
                    "Low price of the day": round(result["l"], 2),
                    "Open price of the day": round(result["o"], 2),
                    "Previous close price": round(result["pc"], 2),
                }
                data.update(data_rates)
            logger.info("формирование полных данных")
            activ_rate.append(data)
            if len(activ_rate) > 5:
                break

        logger.info("сформирован список из 5 первых активов в т.ч. стоимость в индексе")
        return activ_rate

    except requests.exceptions.HTTPError:
        if 500 <= response.status_code < 600:  # type: ignore[union-attr]
            logger.error("Произошла ошибка сервера")
            return "Server Error"
        elif 400 <= response.status_code < 500:  # type: ignore[union-attr]
            logger.error(f"Произошла клиентская ошибка {response.status_code}")  # type: ignore[union-attr]
            return f"Client Error: {response.status_code}"  # type: ignore[union-attr]
