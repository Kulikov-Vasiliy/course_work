import datetime
import logging
from typing import Optional

import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import xlsxwriter  # type: ignore[import-untyped]
from dateutil.relativedelta import relativedelta

file_path_param_r = "../data/operations.xlsx"


logger = logging.getLogger("reports")
log = (
    "..",
    "logs",
    "reports.log",
)
file_handler = logging.FileHandler(
    "../logs/reports.log",
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """возвращает расходы по выбранной категории
    за 3 последних месяца от заданного/текущего"""
    def decorator(func):  # type: ignore[no-untyped-def]
        def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
            result = func(*args, **kwargs)
            transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S")
            logger.info("фильтрация дат и очистка категорий от пустых значений")
            day = transactions["Дата операции"].dt.day
            month = transactions["Дата операции"].dt.month
            filtered_data = transactions[
                (transactions["Дата операции"].dt.month == month) & (transactions["Дата операции"].dt.day == day)
            ]
            filtered_data = filtered_data.dropna(subset=["Категория"])

            logger.info("получение точки начала периода")
            if filtered_data["Дата операции"].dt.day.isin(day).any():
                specific_date = pd.to_datetime(date).date()
                three_months_ago = specific_date  - relativedelta(months=3)
                filtered_data_start = transactions[
                    (transactions["Дата операции"].dt.date >= three_months_ago) &
                    (transactions["Дата операции"].dt.date <= specific_date)
                    ]

            else:
                month_offset = datetime.datetime.today() - relativedelta(months=3)
                current_day = datetime.datetime.today()
                filtered_data_start = transactions[
                    transactions["Дата операции"].apply(lambda x: x >= month_offset.month)
                    & (transactions["Дата операции"].dt.day == current_day)
                ]

            logger.info("подбор необходимых данных")
            filter_result = filtered_data_start[
                filtered_data_start.notna().any(axis=1)  # Проверка на ненулевые значения во всех колонках
                & (filtered_data_start["Сумма операции"] < 0)  # Сумма операции отрицательна
                & (filtered_data_start["Категория"] == category)  # Категория равна заданной
            ]
            filter_result = filter_result.copy()
            resulted = filter_result[
                [
                    "Дата платежа",
                    "Номер карты",
                    "Статус",
                    "Сумма операции",
                    "Кэшбэк",
                    "MCC",
                    "Категория",
                    "Описание",
                    "Округление на инвесткопилку",
                    "Бонусы (включая кэшбэк)",
                ]
            ]
            resulted = resulted.copy()
            resulted["Номер карты"] = resulted["Номер карты"].apply(
                lambda x: x.replace("*", "") if isinstance(x, str) else x
            )
            resulted["Кэшбэк"] = resulted["Кэшбэк"].fillna(round(abs(resulted["Сумма операции"]) / 100, 2))
            resulted["Бонусы (включая кэшбэк)"] = np.where(
                resulted["Бонусы (включая кэшбэк)"].isna(),
                round(abs(resulted["Сумма операции"]) / 100, 2),  # Если NaN, присваиваем новое значение
                round(
                    resulted["Бонусы (включая кэшбэк)"] + abs(resulted["Сумма операции"]) / 100,
                    2,
                ),
            )  # Иначе, складываем
            resulted.replace([np.inf, -np.inf], np.nan).fillna(0)

            return result

        return wrapper

    return decorator


@spending_by_category(
    transactions=pd.read_excel(file_path_param_r, sheet_name="Отчет по операциям"),
    category="Аптеки",
    date="2021-12-30 08:16:00",
)
def categories(transactions, category, date):  # type: ignore[no-untyped-def]

    logger.info("формирование файла")
    workbook = xlsxwriter.Workbook("../data/transactions.xlsx")
    worksheet = workbook.add_worksheet()
    for col_num, col_data in enumerate(resulted.columns):
        worksheet.set_column(col_num, col_num, 50)

    # Запись заголовков
    for col_num, col_name in enumerate(resulted.columns):
        worksheet.write(0, col_num, col_name)

    # Запись данных
    for row_num, row_data in enumerate(resulted.values):
        worksheet.write_row(row_num + 1, 0, row_data)

    workbook.close()
    print("В data сформирован файл с результатом")


# def write_to_file(resulted):
#     """Запись в xlsx-файл"""

