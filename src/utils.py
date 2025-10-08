from datetime import datetime
import pandas as pd
from pandas import DataFrame
from collections import Counter
import numpy as np
import re


def greet_result() -> str:
    """Приветствие в формате «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи»"""
    now = datetime.now()
    time_form = now.strftime("%H:%M:%S")  # только время

    if "07:00:00" <= time_form <= "10:00:00":
        greet = "ое утро"
    elif "10:00:01" <= time_form <= "16:00:00":
        greet = "ый день"
    elif "16:00:01" <= time_form <= "22:00:00":
        greet = "ый вечер"
    else:
        greet = "ой ночи"

    return f'Добр{greet}'


def get_date_time(date_time: str, date_format: str = "%Y-%m-%d %H:%M:%S")->list[str]:
    """Меняет формат строки и фильтрует от начала месяца до указанного числа"""
    dt = datetime.strptime(date_time, date_format)
    month_start = dt.replace(day=1)

    return [month_start.strftime("%d.%m.%Y %H:%M:%S"),
            dt.strftime("%d.%m.%Y %H:%M:%S")]


def get_path_period(path_file:str, time_period: list) -> DataFrame:
    df = pd.read_excel(path_file, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    start_period = datetime.strptime(time_period[0], "%d.%m.%Y %H:%M:%S")
    last_date = datetime.strptime(time_period[1], "%d.%m.%Y %H:%M:%S")
    filtered_df = df[
        (df["Дата операции"] >= start_period) &
        (df["Дата операции"] <= last_date)
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
        [
            "Номер карты",
            "Сумма операции",
            "Кэшбэк",
            "Сумма операции с округлением"
         ]
    ]

    for i, row in card_sorted.iterrows():
        sorted_df["Сумма операции"] = pd.to_numeric(sorted_df["Сумма операции"], errors="coerce")
        sorted_df["Сумма операции с округлением"] = pd.to_numeric(sorted_df["Сумма операции с округлением"], errors="coerce")
        sorted_df["Кэшбэк"] = pd.to_numeric(sorted_df["Кэшбэк"], errors="coerce")  # dropna(how="all")  # .unique()

        if pd.isna(row["Номер карты"]):
            continue

        last_digit = str(row["Номер карты"]).strip()

        if last_digit not in card_spent:
            card_spent[last_digit] = {"total_spent": 0, "cashback": 0}

        if row["Сумма операции"] < 0:
            total_spent = row["Сумма операции с округлением"]
        else:
            total_spent = row["Сумма операции"]

        cashback = (row["Сумма операции"] / 100) if pd.isna(row["Кэшбэк"]) else row["Кэшбэк"]
        cashback = abs(cashback)

        card_spent[last_digit]["total_spent"] += total_spent
        card_spent[last_digit]["cashback"] += cashback

    for card, values in card_spent.items():
        card_info = {
            "last_digits": card,
            "total_spent": round(values['total_spent'], 2),
            "cashback": round(values['cashback'], 2)
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
    transaction_sorted = sorted_df[
        [
            "Дата платежа",
            "Сумма операции",
            "Категория",
            "Описание"
        ]
    ]
    count = Counter()   # type: ignore[var-annotated]
    for i, row in transaction_sorted.iterrows():
        pass
        """
        for operation in data:
            desc = operation.get("description", "")
            for category in categories:
                if category.lower() in desc.lower():
                    counts[category] += 1

        return dict(counts)"""
