import pytest
import pandas as pd


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