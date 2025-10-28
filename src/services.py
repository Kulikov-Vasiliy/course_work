# функция сервисов- Выгодные категории повышенного кэшбэка
import json
import logging
import math
from json import JSONDecodeError
import os

import pandas as pd

file_path_param_s = os.path.join(os.path.dirname(__file__),"../data/operations.xlsx")


logger = logging.getLogger("services")
log = os.path.join(os.path.dirname(__file__),'..', 'logs', 'services.log')
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__),"../logs/services.log"),
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def analyze_cashback(file_path: str, year: int, month: int) -> str:
    """Анализирует выгодные категории возврата дс"""
    df = pd.read_excel(file_path, sheet_name="Отчет по операциям")
    logger.info("фильтрация данных")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_data = df[(df["Дата операции"].dt.year == year) & (df["Дата операции"].dt.month == month)]
    filtered_data = filtered_data.dropna(subset=["Категория"])

    try:
        result: dict[str, float] = {}
        logger.info("проверка отфильтрованных данных")
        for i, row in filtered_data.iterrows():
            if row["Сумма платежа"] >= 0:
                continue  # Пропускаем доходы

            category = row["Категория"]
            logger.info("расчет сумм возврата дс по категориям")
            if math.isnan(row["Кэшбэк"]):
                # Случай 1: Кэшбэк не указан - вычисляем как 1% от суммы
                cashback_amount = abs(row["Сумма платежа"]) * 0.01
            else:
                # Случай 2: Кэшбэк указан - используем его
                cashback_amount = abs(row["Кэшбэк"])

            # Суммируем кэшбэк по категориям
            if category in result:
                result[category] += cashback_amount
            else:
                result[category] = cashback_amount

        logger.info("формирование ответа")
        # Округляем результаты
        result = {category: round(amount, 2) for category, amount in result.items()}
        logger.info("успешно сформирован ответ")
        return json.dumps(result, ensure_ascii=False, indent=4)

    except JSONDecodeError:
        logger.error("Произошла ошибка кодирования ")
        return "ошибка формирования ответа"
