# запуск функционала
from src.services import analyze_cashback, file_path_param
from src.views import greetings

if __name__ == "__main__":
    print(greetings("2021-12-30 08:16:00"))
    print(analyze_cashback(file_path_param, 2021, 5))
