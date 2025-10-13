import io
import sys
from src.views import greetings


# Тестируем функцию, которая использует print

def test_greetings_output(capsys):
    # Вызываем функцию, которая использует print
    greetings("2021-12-30 08:16:00")

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что в выводе содержится ожидаемый текст
    assert "ожидаемый результат" in captured.out