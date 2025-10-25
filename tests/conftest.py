import pytest

import pandas as pd

import xlsxwriter

import openpyxl

from pathlib import Path


@pytest.fixture
def greet_tonight():
    return {
    "greeting": "Добрый вечер",
    "cards": [
        {
            "last_digits": "*7197",
            "total_spent": 24422.02,
            "cashback": 244.22
        },
        {
            "last_digits": "*5091",
            "total_spent": 17071.6,
            "cashback": 170.72
        },
        {
            "last_digits": "*4556",
            "total_spent": 27275.7,
            "cashback": 417.15
        }
    ],
    "top_transactions": [
        {
            "date": "13.12.2021",
            "amount": -99.0,
            "category": "Фастфуд",
            "description": "IP Yakubovskaya M.V."
        },
        {
            "date": "01.12.2021",
            "amount": -99.22,
            "category": "Супермаркеты",
            "description": "Дикси"
        },
        {
            "date": "01.12.2021",
            "amount": -199.0,
            "category": "Дом и ремонт",
            "description": "Строитель"
        },
        {
            "date": "02.12.2021",
            "amount": -1.07,
            "category": "Каршеринг",
            "description": "Ситидрайв"
        },
        {
            "date": "21.12.2021",
            "amount": -15.0,
            "category": "Другое",
            "description": "Google"
        }
    ],
    "currency_rates": [
        {
            "currency": "CNY",
            "rate": 11.44
        },
        {
            "currency": "EUR",
            "rate": 94.83
        }
    ],
    "stock_prices": [
        {
            "stock": "FOX",
            "company_name": "Fox Corporation(Class B)",
            "sector": "Communication Services",
            "price": 51.4,
            "High price of the day": 53.11,
            "Low price of the day": 51.25,
            "Open price of the day": 53.11,
            "Previous close price": 52.66
        },
        {
            "stock": "AMP",
            "company_name": "Ameriprise Financial",
            "sector": "Financials",
            "price": 479.43,
            "High price of the day": 496.16,
            "Low price of the day": 478.56,
            "Open price of the day": 493.23,
            "Previous close price": 491.38
        },
        {
            "stock": "ETR",
            "company_name": "Entergy",
            "sector": "Utilities",
            "price": 95.26,
            "High price of the day": 97.4,
            "Low price of the day": 95,
            "Open price of the day": 95.94,
            "Previous close price": 95.62
        },
        {
            "stock": "ABBV",
            "company_name": "AbbVie",
            "sector": "Health Care",
            "price": 230.5,
            "High price of the day": 234.68,
            "Low price of the day": 230.5,
            "Open price of the day": 231.51,
            "Previous close price": 230.69
        },
        {
            "stock": "PFG",
            "company_name": "Principal Financial Group",
            "sector": "Financials",
            "price": 79.42,
            "High price of the day": 83.72,
            "Low price of the day": 79.36,
            "Open price of the day": 83.28,
            "Previous close price": 82.69
        },
        {
            "stock": "TDG",
            "company_name": "TransDigm Group",
            "sector": "Industrials",
            "price": 1277.99,
            "High price of the day": 1287.8,
            "Low price of the day": 1270,
            "Open price of the day": 1273.14,
            "Previous close price": 1275.44
        }
    ]
}



@pytest.fixture
def greet_morning():
    return {
    "greeting": "Доброе утро",
    "cards": [
        {
            "last_digits": "*7197",
            "total_spent": 24422.02,
            "cashback": 244.22
        },
        {
            "last_digits": "*5091",
            "total_spent": 17071.6,
            "cashback": 170.72
        },
        {
            "last_digits": "*4556",
            "total_spent": 27275.7,
            "cashback": 417.15
        }
    ],
    "top_transactions": [
        {
            "date": "13.12.2021",
            "amount": -99.0,
            "category": "Фастфуд",
            "description": "IP Yakubovskaya M.V."
        },
        {
            "date": "01.12.2021",
            "amount": -99.22,
            "category": "Супермаркеты",
            "description": "Дикси"
        },
        {
            "date": "01.12.2021",
            "amount": -199.0,
            "category": "Дом и ремонт",
            "description": "Строитель"
        },
        {
            "date": "02.12.2021",
            "amount": -1.07,
            "category": "Каршеринг",
            "description": "Ситидрайв"
        },
        {
            "date": "21.12.2021",
            "amount": -15.0,
            "category": "Другое",
            "description": "Google"
        }
    ],
    "currency_rates": [
        {
            "currency": "CNY",
            "rate": 11.44
        },
        {
            "currency": "EUR",
            "rate": 94.83
        }
    ],
    "stock_prices": [
        {
            "stock": "FOX",
            "company_name": "Fox Corporation(Class B)",
            "sector": "Communication Services",
            "price": 51.4,
            "High price of the day": 53.11,
            "Low price of the day": 51.25,
            "Open price of the day": 53.11,
            "Previous close price": 52.66
        },
        {
            "stock": "AMP",
            "company_name": "Ameriprise Financial",
            "sector": "Financials",
            "price": 479.43,
            "High price of the day": 496.16,
            "Low price of the day": 478.56,
            "Open price of the day": 493.23,
            "Previous close price": 491.38
        },
        {
            "stock": "ETR",
            "company_name": "Entergy",
            "sector": "Utilities",
            "price": 95.26,
            "High price of the day": 97.4,
            "Low price of the day": 95,
            "Open price of the day": 95.94,
            "Previous close price": 95.62
        },
        {
            "stock": "ABBV",
            "company_name": "AbbVie",
            "sector": "Health Care",
            "price": 230.5,
            "High price of the day": 234.68,
            "Low price of the day": 230.5,
            "Open price of the day": 231.51,
            "Previous close price": 230.69
        },
        {
            "stock": "PFG",
            "company_name": "Principal Financial Group",
            "sector": "Financials",
            "price": 79.42,
            "High price of the day": 83.72,
            "Low price of the day": 79.36,
            "Open price of the day": 83.28,
            "Previous close price": 82.69
        },
        {
            "stock": "TDG",
            "company_name": "TransDigm Group",
            "sector": "Industrials",
            "price": 1277.99,
            "High price of the day": 1287.8,
            "Low price of the day": 1270,
            "Open price of the day": 1273.14,
            "Previous close price": 1275.44
        }
    ]
}


@pytest.fixture
def greet_morning_print():
    return {
    "cards": [
        {
            "last_digits": "*7197",
            "total_spent": 24422.02,
            "cashback": 244.22
        },
        {
            "last_digits": "*5091",
            "total_spent": 17071.6,
            "cashback": 170.72
        },
        {
            "last_digits": "*4556",
            "total_spent": 27275.7,
            "cashback": 417.15
        }
    ],
    "top_transactions": [
        {
            "date": "13.12.2021",
            "amount": -99.0,
            "category": "Фастфуд",
            "description": "IP Yakubovskaya M.V."
        },
        {
            "date": "01.12.2021",
            "amount": -99.22,
            "category": "Супермаркеты",
            "description": "Дикси"
        },
        {
            "date": "01.12.2021",
            "amount": -199.0,
            "category": "Дом и ремонт",
            "description": "Строитель"
        },
        {
            "date": "02.12.2021",
            "amount": -1.07,
            "category": "Каршеринг",
            "description": "Ситидрайв"
        },
        {
            "date": "21.12.2021",
            "amount": -15.0,
            "category": "Другое",
            "description": "Google"
        }
    ],
    "currency_rates": [
        {
            "currency": "CNY",
            "rate": 11.44
        },
        {
            "currency": "EUR",
            "rate": 94.83
        }
    ],
    "stock_prices": [
        {
            "stock": "FOX",
            "company_name": "Fox Corporation(Class B)",
            "sector": "Communication Services",
            "price": 51.4,
            "High price of the day": 53.11,
            "Low price of the day": 51.25,
            "Open price of the day": 53.11,
            "Previous close price": 52.66
        },
        {
            "stock": "AMP",
            "company_name": "Ameriprise Financial",
            "sector": "Financials",
            "price": 479.43,
            "High price of the day": 496.16,
            "Low price of the day": 478.56,
            "Open price of the day": 493.23,
            "Previous close price": 491.38
        },
        {
            "stock": "ETR",
            "company_name": "Entergy",
            "sector": "Utilities",
            "price": 95.26,
            "High price of the day": 97.4,
            "Low price of the day": 95,
            "Open price of the day": 95.94,
            "Previous close price": 95.62
        },
        {
            "stock": "ABBV",
            "company_name": "AbbVie",
            "sector": "Health Care",
            "price": 230.5,
            "High price of the day": 234.68,
            "Low price of the day": 230.5,
            "Open price of the day": 231.51,
            "Previous close price": 230.69
        },
        {
            "stock": "PFG",
            "company_name": "Principal Financial Group",
            "sector": "Financials",
            "price": 79.42,
            "High price of the day": 83.72,
            "Low price of the day": 79.36,
            "Open price of the day": 83.28,
            "Previous close price": 82.69
        },
        {
            "stock": "TDG",
            "company_name": "TransDigm Group",
            "sector": "Industrials",
            "price": 1277.99,
            "High price of the day": 1287.8,
            "Low price of the day": 1270,
            "Open price of the day": 1273.14,
            "Previous close price": 1275.44
        }
    ]
}



@pytest.fixture
def greet_day():
    return {
    "greeting": "Добрый день",
    "cards": [
        {
            "last_digits": "*7197",
            "total_spent": 24422.02,
            "cashback": 244.22
        },
        {
            "last_digits": "*5091",
            "total_spent": 17071.6,
            "cashback": 170.72
        },
        {
            "last_digits": "*4556",
            "total_spent": 27275.7,
            "cashback": 417.15
        }
    ],
    "top_transactions": [
        {
            "date": "13.12.2021",
            "amount": -99.0,
            "category": "Фастфуд",
            "description": "IP Yakubovskaya M.V."
        },
        {
            "date": "01.12.2021",
            "amount": -99.22,
            "category": "Супермаркеты",
            "description": "Дикси"
        },
        {
            "date": "01.12.2021",
            "amount": -199.0,
            "category": "Дом и ремонт",
            "description": "Строитель"
        },
        {
            "date": "02.12.2021",
            "amount": -1.07,
            "category": "Каршеринг",
            "description": "Ситидрайв"
        },
        {
            "date": "21.12.2021",
            "amount": -15.0,
            "category": "Другое",
            "description": "Google"
        }
    ],
    "currency_rates": [
        {
            "currency": "CNY",
            "rate": 11.44
        },
        {
            "currency": "EUR",
            "rate": 94.83
        }
    ],
    "stock_prices": [
        {
            "stock": "FOX",
            "company_name": "Fox Corporation(Class B)",
            "sector": "Communication Services",
            "price": 51.4,
            "High price of the day": 53.11,
            "Low price of the day": 51.25,
            "Open price of the day": 53.11,
            "Previous close price": 52.66
        },
        {
            "stock": "AMP",
            "company_name": "Ameriprise Financial",
            "sector": "Financials",
            "price": 479.43,
            "High price of the day": 496.16,
            "Low price of the day": 478.56,
            "Open price of the day": 493.23,
            "Previous close price": 491.38
        },
        {
            "stock": "ETR",
            "company_name": "Entergy",
            "sector": "Utilities",
            "price": 95.26,
            "High price of the day": 97.4,
            "Low price of the day": 95,
            "Open price of the day": 95.94,
            "Previous close price": 95.62
        },
        {
            "stock": "ABBV",
            "company_name": "AbbVie",
            "sector": "Health Care",
            "price": 230.5,
            "High price of the day": 234.68,
            "Low price of the day": 230.5,
            "Open price of the day": 231.51,
            "Previous close price": 230.69
        },
        {
            "stock": "PFG",
            "company_name": "Principal Financial Group",
            "sector": "Financials",
            "price": 79.42,
            "High price of the day": 83.72,
            "Low price of the day": 79.36,
            "Open price of the day": 83.28,
            "Previous close price": 82.69
        },
        {
            "stock": "TDG",
            "company_name": "TransDigm Group",
            "sector": "Industrials",
            "price": 1277.99,
            "High price of the day": 1287.8,
            "Low price of the day": 1270,
            "Open price of the day": 1273.14,
            "Previous close price": 1275.44
        }
    ]
}



@pytest.fixture
def greet_night():
    return {
    "greeting": "Доброй ночи",
    "cards": [
        {
            "last_digits": "*7197",
            "total_spent": 24422.02,
            "cashback": 244.22
        },
        {
            "last_digits": "*5091",
            "total_spent": 17071.6,
            "cashback": 170.72
        },
        {
            "last_digits": "*4556",
            "total_spent": 27275.7,
            "cashback": 417.15
        }
    ],
    "top_transactions": [
        {
            "date": "13.12.2021",
            "amount": -99.0,
            "category": "Фастфуд",
            "description": "IP Yakubovskaya M.V."
        },
        {
            "date": "01.12.2021",
            "amount": -99.22,
            "category": "Супермаркеты",
            "description": "Дикси"
        },
        {
            "date": "01.12.2021",
            "amount": -199.0,
            "category": "Дом и ремонт",
            "description": "Строитель"
        },
        {
            "date": "02.12.2021",
            "amount": -1.07,
            "category": "Каршеринг",
            "description": "Ситидрайв"
        },
        {
            "date": "21.12.2021",
            "amount": -15.0,
            "category": "Другое",
            "description": "Google"
        }
    ],
    "currency_rates": [
        {
            "currency": "CNY",
            "rate": 11.44
        },
        {
            "currency": "EUR",
            "rate": 94.83
        }
    ],
    "stock_prices": [
        {
            "stock": "FOX",
            "company_name": "Fox Corporation(Class B)",
            "sector": "Communication Services",
            "price": 51.4,
            "High price of the day": 53.11,
            "Low price of the day": 51.25,
            "Open price of the day": 53.11,
            "Previous close price": 52.66
        },
        {
            "stock": "AMP",
            "company_name": "Ameriprise Financial",
            "sector": "Financials",
            "price": 479.43,
            "High price of the day": 496.16,
            "Low price of the day": 478.56,
            "Open price of the day": 493.23,
            "Previous close price": 491.38
        },
        {
            "stock": "ETR",
            "company_name": "Entergy",
            "sector": "Utilities",
            "price": 95.26,
            "High price of the day": 97.4,
            "Low price of the day": 95,
            "Open price of the day": 95.94,
            "Previous close price": 95.62
        },
        {
            "stock": "ABBV",
            "company_name": "AbbVie",
            "sector": "Health Care",
            "price": 230.5,
            "High price of the day": 234.68,
            "Low price of the day": 230.5,
            "Open price of the day": 231.51,
            "Previous close price": 230.69
        },
        {
            "stock": "PFG",
            "company_name": "Principal Financial Group",
            "sector": "Financials",
            "price": 79.42,
            "High price of the day": 83.72,
            "Low price of the day": 79.36,
            "Open price of the day": 83.28,
            "Previous close price": 82.69
        },
        {
            "stock": "TDG",
            "company_name": "TransDigm Group",
            "sector": "Industrials",
            "price": 1277.99,
            "High price of the day": 1287.8,
            "Low price of the day": 1270,
            "Open price of the day": 1273.14,
            "Previous close price": 1275.44
        }
    ]
}


@pytest.fixture
def same():
    return {
        "date": "21.12.2021",
        "Сумма операции": 100.0,  # Убедись, что ключи соответствуют ожиданиям
        "category": "Переводы",
        "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    }

@pytest.fixture
def summed():
    return 1198.23 + 100.0


@pytest.fixture
def categories():
    return {
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
}


# Фикстура, которая предоставляет путь к временному файлу для каждого теста.
@pytest.fixture
def workbook_path(tmp_path: Path):
    return tmp_path / "test_output.xlsx"


# Фикстура, которая создаёт и закрывает рабочую книгу.
@pytest.fixture
def test_workbook(workbook_path: Path):
    workbook = xlsxwriter.Workbook(workbook_path)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Дата платежа")
    worksheet.write(1, 0, "27.12.2021")
    worksheet.write(0, 1, "Номер карты")
    worksheet.write(1, 1, 5091)
    worksheet.write(0, 2, "Статус")
    worksheet.write(1, 2, "OK")
    worksheet.write(0, 3, "Сумма операции")
    worksheet.write(1, 3, -123)
    worksheet.write(0, 4, "Кэшбэк")
    worksheet.write(1, 4, 1.23)
    worksheet.write(0, 5, "MCC")
    worksheet.write(1, 5, 5912)
    worksheet.write(0, 6, "Категория")
    worksheet.write(1, 6, "Аптеки")
    worksheet.write(0, 7, "Описание")
    worksheet.write(1, 7, "Apteka 23")
    worksheet.write(0, 8, "Округление на инвесткопилку")
    worksheet.write(1, 8, 0)
    worksheet.write(0, 9, "Бонусы (включая кэшбэк)")
    worksheet.write(1, 9, 2.23)

    workbook.close()
    return workbook_path
