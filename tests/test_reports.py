from pathlib import Path

from unittest.mock import patch

import pytest

import pandas as pd

from src.reports import spending_by_category

from freezegun import freeze_time

import logging

import openpyxl

from pandas.testing import assert_frame_equal

from datetime import datetime

from dateutil.relativedelta import relativedelta


@pytest.fixture(autouse=True)
def disable_logging():
    logging.disable(logging.CRITICAL)


def test_workbook_creation(test_workbook: Path):
    assert test_workbook.exists()


def test_workbook_content(test_workbook: Path):
    wb = openpyxl.load_workbook(test_workbook)
    sheet = wb.active

    # Проверяем содержимое ячеек
    assert sheet['A1'].value == "Дата платежа"
    assert sheet['A2'].value == "27.12.2021"
    assert sheet['B1'].value == "Номер карты"
    assert sheet['B2'].value == 5091
    assert sheet['C1'].value == "Статус"
    assert sheet['C2'].value == "OK"
    assert sheet['D1'].value == "Сумма операции"
    assert sheet['D2'].value == -123
    assert sheet['E1'].value == "Кэшбэк"
    assert sheet['E2'].value == 1.23
    assert sheet['F1'].value == "MCC"
    assert sheet['F2'].value == 5912
    assert sheet['G1'].value == "Категория"
    assert sheet['G2'].value == "Аптеки"
    assert sheet['H1'].value == "Описание"
    assert sheet['H2'].value == "Apteka 23"
    assert sheet['I1'].value == "Округление на инвесткопилку"
    assert sheet['I2'].value == 0
    assert sheet['J1'].value == "Бонусы (включая кэшбэк)"
    assert sheet['J2'].value == 2.23

    wb.close()


MOCK_DATA = {
    'Дата операции': ['2025-09-01 10:00:00', '2025-08-15 12:00:00', '2025-09-20 15:30:00', '2025-06-01 09:00:00'],
    'Дата платежа': ['01.09.2025', '15.08.2025', '20.09.2025', '01.06.2025'],
    'Номер карты': ['*1234', '*5678', '*1234', '*1234'],
    'Статус': ['OK', 'OK', 'OK', 'OK'],
    'Сумма операции': [-100.0, -50.0, -200.0, -30.0],
    'Валюта операции': ['RUB', 'RUB', 'RUB', 'RUB'],
    'Сумма платежа': [-100.0, -50.0, -200.0, -30.0],
    'Валюта платежа': ['RUB', 'RUB', 'RUB', 'RUB'],
    'Кэшбэк': [None, 2.5, None, 1.0],
    'Категория': ['Еда', 'Одежда', 'Еда', 'Еда'],
    'MCC': [111, 222, 111, 111],
    'Описание': ['Кафе', 'Магазин', 'Ресторан', 'Магазин'],
    'Бонусы (включая кэшбэк)': [None, 2.5, 2.0, 1.0],
    'Округление на инвесткопилку': [0, 0, 0, 0],
    'Сумма операции с округлением': [100.0, 50.0, 200.0, 30.0]
    }
MOCK_DF = pd.DataFrame(MOCK_DATA)
MOCK_DF['Дата операции'] = pd.to_datetime(MOCK_DF['Дата операции'])


@freeze_time("2025-09-25")
def test_spending_by_category_with_freezegun():
    # Создаем тестовый DataFrame
    test_data = {
        'Дата операции': [
            datetime(2025, 9, 20),
            datetime(2025, 8, 25),
            datetime(2025, 6, 20),
            datetime(2025, 5, 25)
        ],
        'Категория': ['Еда', 'Еда', 'Еда', 'Еда'],
        'Сумма операции': [-100, -50, -30, -20]
    }
    df = pd.DataFrame(test_data)

    # Применяем декоратор
    @spending_by_category(transactions=df, category='Еда')
    def decorated_function():
        pass

    # Запускаем тест
    decorated_function()


@patch('pandas.read_excel', return_value=MOCK_DF)
@patch('xlsxwriter.Workbook')
@patch('src.reports.datetime')
def test_spending_by_category_decorator_logic(mock_datetime, mock_workbook, mock_read_excel):
    # Мокируем текущую дату
    mock_datetime.today.return_value = datetime(2025, 9, 25)

    # Функция, которую будет оборачивать декоратор
    @spending_by_category(transactions=None, category='Одежда', date='2025-09-25 00:00:00')
    def decorated_function():
        return "Исходный результат"

    # Вызываем декорированную функцию
    result = decorated_function()

    # Проверяем, что pandas.read_excel был вызван
    mock_read_excel.assert_called_once()

    mock_workbook.assert_called_once_with("C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/pythonProject/data/transactions.xlsx")

    # Проверка того, что исходный результат возвращается
    assert result == "Исходный результат"
