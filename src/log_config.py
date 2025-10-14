import logging

logger = logging.getLogger("utils")
log = (
    "C",
    "Users",
    "Я",
    "Desktop",
    "ДЛЯ РАБОТЫ",
    "pythonProject",
    "course_work",
    "pythonProject",
    "course_work",
    "pythonProject",
    "logs",
    "utils.log",
)
file_handler = logging.FileHandler(
    "C:/Users/Я/Desktop/ДЛЯ РАБОТЫ/pythonProject/course_work/"
    "pythonProject/logs/utils.log",
    "w",
    encoding="utf-8",
)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
