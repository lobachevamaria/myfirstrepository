import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразовать JSON-файл в CSV.

    Подаётся:
        json_path: путь к JSON-файлу (строка или Path).
        csv_path: путь к создаваемому CSV-файлу (строка или Path).
        encoding: кодировка для чтения и записи файлов (по умолчанию "utf-8").

    Действие:
        - Читает JSON.
        - Определяет заголовки по ключам первого словаря.
        - Создаёт CSV с заголовком и строками из JSON.

    Ошибки:
        FileNotFoundError: Если JSON-файл отсутствует.
        ValueError: Если JSON пустой, не является списком словарей
                    или имеет неподдерживаемую структуру.
                    Если JSON-файл содержит синтаксические ошибки.
    """

    file_json = Path(json_path)

    if not file_json.exists():
        raise FileNotFoundError("файл не найден")

    try:
        with file_json.open("r", encoding="utf-8") as f:
            dano = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("неподдерживаемая структура")

    except not isinstance(dano, list):
        raise ValueError("JSON должен быть быть в виде списка объектов")

    except len(dano) == 0:
        raise ValueError("JSON файл пуст")

    except not all(isinstance(item, dict) for item in dano):
        raise ValueError("Каждый элемент JSON должны быть словарями")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        header = tuple(dano[0].keys())
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(dano)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразовать CSV-файл в JSON.

    Подаётся:
        csv_path: путь к CSV-файлу (строка или Path).
        json_path: путь к создаваемому JSON-файлу (строка или Path).
        encoding: кодировка для чтения и записи файлов (по умолчанию "utf-8").

    Действие:
        - Читает CSV с заголовком.
        - Преобразует строки CSV в список словарей.
        - Записывает JSON с отступами для удобного чтения.

    Ошибки:
        FileNotFoundError: Если CSV-файл отсутствует.
        ValueError: Если CSV не содержит заголовков или пуст.
                    Если структура CSV-файла некорректна.
    """
    file_csv = Path(csv_path)

    if not file_csv.exists():
        raise FileNotFoundError("Файл не найден")

    if file_csv.suffix != ".csv":
        raise ValueError("Неверный тип данных")

    with open(file_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("Отсутствуют заголовки в файле")
        dano = list(reader)
    if len(dano) == 0:
        raise ValueError("Пустой файл")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dano, f, ensure_ascii=False, indent=2)
