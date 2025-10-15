import datetime

import logging

from typing import Optional

import pandas as pd


file_path_param = (
    "C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
    "pythonProject/data/operations.xlsx"
)


logger = logging.getLogger("views")
log = (
    "C", "Users", "Я", "Desktop", "ДЛЯ РАБОТЫ", "pythonProject",
    "course_work", "pythonProject", "course_work", "pythonProject",
    "logs", "reports.log",
)
file_handler = logging.FileHandler(
    "C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
    "pythonProject/logs/reports.log","w", encoding="utf-8",
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
    transactions = pd.read_excel(file_path_param, sheet_name="Отчет по операциям")

    def decorator(func):
       def wrapper(*args, **kwargs):
           result = func(*args, **kwargs)
           transactions["Дата операции"] = pd.to_datetime(
               transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S"
           )

           for day, month in transactions["Дата операции"]:
               filtered_data = transactions[
               (transactions["Дата операции"].dt.month == month) & (transactions["Дата операции"].dt.day == day)
               ]
               filtered_data = filtered_data.dropna(subset=["Категория"])

               if day in date.split(" ")[1].split("-")[2]:
                   filtered_data_start = transactions[
                   (transactions["Дата операции"].dt.replace(month=int(date.split(" ")[1].split("-")[1]) -3))
                   &
                   (transactions["Дата операции"].dt.day == day)
                   ]
               else:
                   filtered_data_start = transactions[
                   (transactions["Дата операции"].dt.replace(month=int(datetime.datetime.now().strftime("%d:%m:%Y").split(".")[1])-3))
                   &
                   (transactions["Дата операции"].dt.day == datetime.datetime.now().strftime("%d:%m:%Y").split(".")[0])
                   ]
               print(filtered_data_start)
               start = filtered_data_start
               for i, row in range(start, filtered_data):
                   if row["Сумма платежа"] >= 0:
                       continue  # Пропускаем доходы
                   if pd.isna(
                      row["Номер карты"]
                      or row["Категория"]
                      or row["Описание"]
                      or row["Дата платежа"]
                      or row["Статус"]
                      or row["Сумма операции"]
                      or row["Кэшбэк"]
                      or row["MCC"]
                      or row["Округление на инвесткопилку"]
                      or row["Бонусы (включая кэшбэк)"]
                   ):
                      continue
                   if row["Категория"] == category:
                       result = filtered_data[
                       ["Номер карты", "Статус", "Сумма операции", "Кэшбэк", "MCC", "Описание", "Округление на инвесткопилку",  "Бонусы (включая кэшбэк)"]
                       ]

           with open("C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
                     "pythonProject/data/transactions.xlsx", "w", encoding="utf-8") as file:
               file.write(result)

           return wrapper
       return decorator


@spending_by_category(transactions=file_path_param, category, date)
def categories(transactions, category , date):
    print(category)
