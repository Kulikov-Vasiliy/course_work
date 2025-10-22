import datetime

import logging

import numpy as np
from dateutil.relativedelta import relativedelta

from typing import Optional

import pandas as pd

import xlsxwriter

file_path_param = (
    "C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
    "pythonProject/data/operations.xlsx"
)


logger = logging.getLogger("reports")
log = (
    "C",
    "Users",
    "Я",
    "Desktop",
    "ДЛЯ РАБОТЫ",
    "pythonProject",
    "course_work",
    "pythonProject",
    "course_work",
    "pythonProject",
    "logs",
    "reports.log",
)
file_handler = logging.FileHandler(
    "C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
    "pythonProject/logs/reports.log",
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def spending_by_category(transactions: pd.DataFrame,
        category: str,
        date: Optional[str] = None) -> pd.DataFrame:
    """возвращает расходы по выбранной категории
    за 3 последних месяца от заданного/текущего"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            df = pd.read_excel(file_path_param, sheet_name="Отчет по операциям")
            df["Дата операции"] = pd.to_datetime(
                df["Дата операции"], format="%d.%m.%Y %H:%M:%S"
            )
            logger.info("фильтрация дат и очистка категорий от пустых значений")
            day = df["Дата операции"].dt.day
            month = df["Дата операции"].dt.month
            filtered_data = df[
                (df["Дата операции"].dt.month == month)
                & (df["Дата операции"].dt.day == day)
                ]
            filtered_data = filtered_data.dropna(subset=["Категория"])

            logger.info("получение точки начала периода")
            if filtered_data["Дата операции"].dt.day.isin(day).any():
                filtered_data_start = df[
                    df["Дата операции"].apply(lambda x: x - relativedelta(months=3)).dt.month
                    & (df["Дата операции"].dt.day == day)
                    ]
            else:
                month_offset = datetime.datetime.today() - relativedelta(months=3)
                current_day = datetime.datetime.today()
                filtered_data_start = df[
                    df["Дата операции"].apply(lambda x: month_offset.month)
                    & (df["Дата операции"].dt.day == current_day)
                    ]

            logger.info("подбор необходимых данных")
            filter_result = filtered_data_start[
                filtered_data_start.notna().any(axis=1) &  # Проверка на ненулевые значения во всех колонках
                (filtered_data_start["Сумма операции"] < 0) &  # Сумма операции отрицательна
                (filtered_data_start["Категория"] == category)  # Категория равна заданной
                ]
            filter_result = filter_result.copy()
            resulted = filter_result[
                    ["Дата платежа",
                    "Номер карты",
                    "Статус",
                    "Сумма операции",
                    "Кэшбэк" if "Кэшбэк" else abs(filter_result["Сумма операции"]) // 100,
                    "MCC",
                    "Категория",
                    "Описание",
                    "Округление на инвесткопилку",
                    "Бонусы (включая кэшбэк)" if "Бонусы (включая кэшбэк)" else abs(filter_result["Сумма операции"]) // 100,
                    ]]
            resulted_cleaned = resulted.replace([np.inf, -np.inf], np.nan).fillna(0)

            logger.info("формирование файла")
            workbook = xlsxwriter.Workbook("C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
                            "pythonProject/data/transactions.xlsx")
            worksheet = workbook.add_worksheet()
            for col_num, col_data in enumerate(resulted_cleaned.columns):
                worksheet.set_column(col_num, col_num, 50)

            # Запись заголовков
            for col_num, col_name in enumerate(resulted_cleaned.columns):
                worksheet.write(0, col_num, col_name)

            # Запись данных
            for row_num, row_data in enumerate(resulted_cleaned.values):
                worksheet.write_row(row_num + 1, 0, row_data)

            workbook.close()

            return result

        return wrapper

    return decorator


@spending_by_category(file_path_param, "Аптеки", "2021-12-30 08:16:00")
def categories(transactions=file_path_param, category="Аптеки", date="2021-12-30 08:16:00"):
    print('готово')
    return "готово"
