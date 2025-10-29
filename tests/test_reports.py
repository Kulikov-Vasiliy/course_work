from pathlib import Path
from unittest.mock import MagicMock,patch
import xlsxwriter
import os

import pytest

import pandas as pd

from src.reports import spending_by_category, categories, file_path_param_r, save_to_file
from pandas.testing import assert_frame_equal

import logging

import openpyxl


@pytest.fixture(autouse=True)
def disable_logging():
    logging.disable(logging.CRITICAL)


def test_categories(test_workbook: Path):
    assert test_workbook.exists()


def test_categories_content(test_workbook: Path):
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
    data = {
        "col1": [1, 2],
        "col2": ["A", "B"]
    }
    df = pd.DataFrame(data)
    # Добавляем атрибут `columns` для имитации DataFrame
    df.columns = ["col1", "col2"]
    return df


@patch("src.reports.spending_by_category")
def test_save_to_file_creates_and_writes_file(mock_spending_by_category, mock_dataframe, tmp_path):
    """
    Тестирует, что декоратор save_to_file корректно записывает данные в файл.
    """
    mock_spending_by_category.return_value = mock_dataframe

    # Создаем путь к временному файлу
    test_file_path = tmp_path / "test_result.xlsx"

    # Декорируем временную функцию нашим декоратором
    @save_to_file(filename=test_file_path)
    def dummy_func(*args, **kwargs):
        pass

    dummy_func(transactions=None)  # Передаем transactions, но mock его игнорирует

    # Проверяем, что файл был создан
    assert os.path.exists(test_file_path)

    # Проверяем, что mock-функция была вызвана
    mock_spending_by_category.assert_called_once()

    # Проверяем содержимое файла (можно прочитать его и убедиться, что оно верное)
    # Это интеграционная проверка. Для юнит-теста можно было бы просто проверить вызовы xlsxwriter.
    read_df = pd.read_excel(test_file_path)
    pd.testing.assert_frame_equal(read_df, mock_dataframe)


@patch("src.reports.xlsxwriter")
@patch("src.reports.spending_by_category")
def test_save_to_file_handles_exception(mock_spending_by_category, mock_xlsxwriter, tmp_path, caplog):
    """
    Тестирует, что декоратор обрабатывает исключение при записи в файл.
    """
    # 1. Настройка моков
    mock_spending_by_category.return_value = pd.DataFrame()

    # Заставляем xlsxwriter.Workbook выбросить исключение при создании
    mock_workbook_constructor = MagicMock()
    mock_workbook_constructor.side_effect = xlsxwriter.exceptions.XlsxWriterException("Test Error")
    mock_xlsxwriter.Workbook = mock_workbook_constructor

    # 2. Декорируем и вызываем функцию
    test_file_path = tmp_path / "test_result.xlsx"

    @save_to_file(filename=test_file_path)
    def dummy_func(*args, **kwargs):
        pass

    # Проверяем, что файл не был создан
    assert not os.path.exists(test_file_path)


def test_categories_function_behavior(capsys):
    """
    Тестирует, что функция categories корректно выводит сообщение в консоль.
    """
    # Вызываем декорируемую функцию, чтобы проверить её собственный вывод
    transactions = pd.read_excel(file_path_param_r, sheet_name="Отчет по операциям")
    categories(transactions, category="Аптека", date="2021-01-01 08:06:00")

    # Захватываем стандартный вывод
    captured = capsys.readouterr()

    # Проверяем, что ожидаемое сообщение было напечатано
    assert "В data сформирован файл с результатом" in captured.out