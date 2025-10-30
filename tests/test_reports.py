from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import xlsxwriter
import os

import pytest

import pandas as pd

from src.reports import spending_by_category, file_path_param_r, save_to_file
from pandas.testing import assert_frame_equal

import logging

import openpyxl


@pytest.fixture(autouse=True)
def disable_logging():
    logging.disable(logging.CRITICAL)


def test_save_to_file(test_workbook: Path):
    assert test_workbook.exists()


def test_save_to_file_content(test_workbook: Path):
    wb = openpyxl.load_workbook(test_workbook)
    sheet = wb.active

    # Проверяем содержимое ячеек
    assert sheet["A1"].value == "Дата платежа"
    assert sheet["A2"].value == "27.12.2021"
    assert sheet["B1"].value == "Номер карты"
    assert sheet["B2"].value == 5091
    assert sheet["C1"].value == "Статус"
    assert sheet["C2"].value == "OK"
    assert sheet["D1"].value == "Сумма операции"
    assert sheet["D2"].value == -123
    assert sheet["E1"].value == "Кэшбэк"
    assert sheet["E2"].value == 1.23
    assert sheet["F1"].value == "MCC"
    assert sheet["F2"].value == 5912
    assert sheet["G1"].value == "Категория"
    assert sheet["G2"].value == "Аптеки"
    assert sheet["H1"].value == "Описание"
    assert sheet["H2"].value == "Apteka 23"
    assert sheet["I1"].value == "Округление на инвесткопилку"
    assert sheet["I2"].value == 0
    assert sheet["J1"].value == "Бонусы (включая кэшбэк)"
    assert sheet["J2"].value == 2.23

    wb.close()


def test_spending_by_category(mocker, spends):
    mocker.patch(
        "pandas.DataFrame",
        return_value=pd.DataFrame(
            {
                "Дата платежа": ["27.12.2021"],
                "Номер карты": [5091],
                "Статус": ["OK"],
                "Сумма операции": [-123],
                "Кэшбэк": [1.23],
                "MCC": [5912],
                "Категория": ["Аптеки"],
                "Описание": ["Apteka 23"],
                "Округление на инвесткопилку": [0],
                "Бонусы (включая кэшбэк)": [2.23],
            }
        ),
    )
    transactions = pd.read_excel(file_path_param_r, sheet_name="Отчет по операциям")
    result = spending_by_category(transactions, "Аптеки", "2021-12-30 08:16:00")
    assert_frame_equal(result, spends)


# Создаем фикстуру для mock-объекта DataFrame, который будет возвращать spending_by_category
@pytest.fixture
def mock_dataframe():
    """Возвращает mock-объект DataFrame с тестовыми данными."""
    data = {"col1": [1, 2], "col2": ["A", "B"]}
    df = pd.DataFrame(data)
    # Добавляем атрибут `columns` для имитации DataFrame
    df.columns = ["col1", "col2"]
    return df
