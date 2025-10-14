import math

import pandas as pd
import json


file_path_param = ("C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
             "pythonProject/data/operations.xlsx")


def analyze_cashback(file_path: str, year: int, month: int) -> str:
    """анализирует выгодные категории возврата дс"""
    df = pd.read_excel(file_path, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_data = df[
        (df["Дата операции"].dt.year == year)
        &
        (df["Дата операции"].dt.month == month)
        ]
    filtered_data = filtered_data.dropna(subset=["Категория"])

    result = {}
    for i, row in filtered_data.iterrows():
        if math.isnan(row["Кэшбэк"]) and row["Сумма платежа"] < 0:
            expenses_by_category = filtered_data.groupby("Категория")["Сумма платежа"].sum()
            expenses_by_category = expenses_by_category[expenses_by_category < 0]
            cashback_by_category = (abs(expenses_by_category) // 100).to_dict()
            result.update(cashback_by_category)

        elif not math.isnan(row["Кэшбэк"]) and row["Сумма платежа"] < 0:
            expenses_by_category = filtered_data.groupby("Категория")["Кэшбэк"].sum()
            expenses_by_category = expenses_by_category[expenses_by_category < 0]
            cashback_by_category = abs(expenses_by_category).to_dict()
            result.update(cashback_by_category)

    return json.dumps(result, ensure_ascii=False, indent= 4)
