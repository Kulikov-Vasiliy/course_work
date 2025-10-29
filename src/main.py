# запуск функционала
import pandas as pd

from src.reports import categories, file_path_param_r, spending_by_category
from src.services import analyze_cashback, file_path_param_s
from src.views import greetings

if __name__ == "__main__":
    # print(greetings("2021-12-30 08:16:00"))
    # print(analyze_cashback(file_path_param_s, 2021, 5))
    transactions = pd.read_excel(file_path_param_r, sheet_name="Отчет по операциям")
    spending_by_category(transactions, "Аптеки", "2021-12-30 08:16:00")
    categories(transactions, "Аптеки", "2021-12-30 08:16:00")
