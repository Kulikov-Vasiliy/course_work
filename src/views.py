# функции генерации json-ответов
import datetime
from time import strftime, time


def greetings():
    """Приветствие в формате «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи»"""
    time_form = datetime.datetime(time.today().now()).strftime("""%Y-%m-%d %H:%M:%S""")
    print(time_form)
    greet = "е"
    for time_i in time_form:
        if "07:00:00" < time_i < "10:00:00":
            greet = "ое утро"
        elif "10:00:01" < time_i < "16:00:00":
            greet = "ый день"
        elif "16:00:01" < time_i < "22:00:00":
            greet = "ый вечер"
        else:
            greet = "ой ночи"

    return f'"Добр{greet}"'


def card_masked():
    """Возвращает номер, траты, возврат средств в формате:
    "cards": [
        {
            "last_digits": "5814",
            "total_spent": 1262.00,
            "cashback": 12.62  (1 rub/100 rub)
        }]"""
    pass

#
# if __name__ == "__main__":
#     print()


"""{
  "greeting": "Добрый день",
  "cards": [
    {
      "last_digits": "5814",
      "total_spent": 1262.00,
      "cashback": 12.62
    },
    {
      "last_digits": "7512",
      "total_spent": 7.94,
      "cashback": 0.08
    }
  ],
  "top_transactions": [
    {
      "date": "21.12.2021",
      "amount": 1198.23,
      "category": "Переводы",
      "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    },
    {
      "date": "20.12.2021",
      "amount": 829.00,
      "category": "Супермаркеты",
      "description": "Лента"
    },
    {
      "date": "20.12.2021",
      "amount": 421.00,
      "category": "Различные товары",
      "description": "Ozon.ru"
    },
    {
      "date": "16.12.2021",
      "amount": -14216.42,
      "category": "ЖКХ",
      "description": "ЖКУ Квартира"
    },
    {
      "date": "16.12.2021",
      "amount": 453.00,
      "category": "Бонусы",
      "description": "Кешбэк за обычные покупки"
    }
  ],
  "currency_rates": [
    {
      "currency": "USD",
      "rate": 73.21
    },
    {
      "currency": "EUR",
      "rate": 87.08
    }
  ],
  "stock_prices": [
    {
      "stock": "AAPL",
      "price": 150.12
    },
    {
      "stock": "AMZN",
      "price": 3173.18
    },
    {
      "stock": "GOOGL",
      "price": 2742.39
    },
    {
      "stock": "MSFT",
      "price": 296.71
    },
    {
      "stock": "TSLA",
      "price": 1007.08
    }
  ]
}"""
