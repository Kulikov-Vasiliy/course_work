# запуск функционала
from src.services import analyze_cashback, file_path_param
from src.views import greetings
from src.reports import file_path_param, categories
import pandas as pd


if __name__ == "__main__":
    print(greetings("2021-12-30 08:16:00"))
    print(analyze_cashback(file_path_param, 2021, 5))
    transactions = pd.read_excel(file_path_param, sheet_name="Отчет по операциям")
    categories(transactions, "Аптеки", "2021-12-30 08:16:00")
