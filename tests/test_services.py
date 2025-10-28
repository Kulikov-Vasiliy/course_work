import pytest
import logging
from json import JSONDecodeError

from src.services import analyze_cashback, file_path_param_s


@pytest.fixture(autouse=True)
def disable_logging():
    logging.disable(logging.CRITICAL)


def test_analyze_cashback_success(mocker, categories):
    mocker.patch("json.dumps",return_value={
    "Супермаркеты": 103.98,
    "Услуги банка": 20.09,
    "Переводы": 160.34,
    "Связь": 7.8,
    "Дом и ремонт": 11.45,
    "Транспорт": 40.23,
    "Книги": 1.13,
    "Наличные": 390.0,
    "Фастфуд": 30.18,
    "Различные товары": 14.45,
    "Сувениры": 1.5,
    "Турагентства": 286.26,
    "Сервис": 0.4,
    "Госуслуги": 6.42,
    "Отели": 147.06,
    "Аптеки": 70.1,
    "Ж/д билеты": 125.86,
    "Красота": 3.0,
    "Рестораны": 0.6
    })
    result = analyze_cashback(file_path_param_s, 2021, 5)
    assert result == categories


def test_analyze_cashback_decode_err(mocker):
    error_instance = JSONDecodeError("msg", "doc", 0)
    mocker.patch("json.dumps", side_effect=error_instance)
    result = analyze_cashback(file_path_param_s, 2021, 5)
    assert result == "ошибка формирования ответа"
