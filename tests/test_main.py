import io
import sys
import pytest
from src.views import greetings


def test_greetings_output(mocker, capsys, greet_morning_print):
    # mocker.patch("builtins.print", return_value=str(greet_morning_print))
    greetings("2021-12-30 08:16:00")
    captured = capsys.readouterr()
    assert "" in captured.out
