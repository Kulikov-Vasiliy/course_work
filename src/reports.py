import datetime

import logging

from dateutil.relativedelta import relativedelta

from typing import Optional

import pandas as pd

from pyexcelerate import Workbook


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


def spending_by_category(
        transactions: pd.DataFrame,
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
            resulted = pd.DataFrame()
            try:
                logger.info("фильтрация дат и очистка категорий от пустых значений")
                for index, row in df.iterrows():
                    day = row["Дата операции"].day
                    month = row["Дата операции"].month
                    filtered_data = df[
                        (df["Дата операции"].dt.month == month)
                        & (df["Дата операции"].dt.day == day)
                    ]
                    filtered_data = filtered_data.dropna(subset=["Категория"])

                    logger.info("получение точки начала периода")
                    if day in filtered_data["Дата операции"].dt.day:
                        filtered_data_start = df[
                            df["Дата операции"].apply(lambda x: x - relativedelta(months=3)).dt.month == month - 3
                            & (df["Дата операции"].dt.day == day)
                        ]
                    else:
                        month_offset = datetime.datetime.today() - relativedelta(months=3)
                        current_day = datetime.datetime.today()
                        filtered_data_start = df[
                            df["Дата операции"].apply(lambda x:  x - relativedelta(months=3)).dt.month == month_offset.month
                            & (df["Дата операции"].dt.day == current_day)
                            ]

                    logger.info("подбор необходимых данных")
                    for i, el in filtered_data_start.iterrows():
                        if pd.isna(
                            el["Номер карты"].strip()
                            or el["Категория"]
                            or el["Описание"]
                            or el["Дата платежа"]
                            or el["Статус"]
                            or el["Сумма операции"] and el["Сумма операции"] >= 0
                            or el["Кэшбэк"]
                            or el["MCC"]
                            or el["Округление на инвесткопилку"]
                            or el["Бонусы (включая кэшбэк)"]
                        ):
                            continue

                        if el["Категория"] == category:
                            resulted = filtered_data[
                                        ["Номер карты",
                                        "Статус",
                                        "Сумма операции",
                                        "Кэшбэк",
                                        "MCC",
                                        "Описание",
                                        "Округление на инвесткопилку",
                                        "Бонусы (включая кэшбэк)",
                                    ]]

                logger.info("формирование файла")
                wb = Workbook()
                wb.new_sheet(data=resulted)
                wb.save(r"C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
                        "pythonProject/data/transactions.xlsx", index=False, header=True)
            except Exception as e:
                logger.error(f"Произошла ошибка кодирования {e}")
                return f"Произошла ошибка {e}"
            return wrapper

        return decorator




@spending_by_category(
    file_path_param,"Аптеки", "2021-12-30 08:16:00"
)
def categories(transactions=file_path_param, category="Аптеки", date="2021-12-30 08:16:00"):
    return "готово"
