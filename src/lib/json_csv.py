import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    file_json=Path(json_path)

    if not file_json.exists():
        return FileNotFoundError("файл не найден")

    try:
        with file_json.open('r',encoding='utf-8') as f:
            dano=json.load(f)
    except json.JSONDecodeError:
        return ValueError("неподдерживаемая структура")

    except not isinstance(dano,list):
        return ValueError("JSON должен быть быть в виде списка объектов")

    except len(dano)==0:
        return ValueError("JSON файл пуст")

    except not all(isinstance(item, dict) for item in dano):
        return ValueError("Каждый элемент JSON должны быть словарями")

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=tuple(dano[0].keys()))
            writer.writeheader()
            writer.writerows(dano)
def csv_to_json(csv_path: str, json_path: str) -> None:
    file_csv=Path(csv_path)

    if not file_csv.exists():
        return FileNotFoundError("Файл не найден")

    if file_csv.suffix != ".csv":
        return ValueError("Неверный тип данных")

    with open(file_csv, "r", encoding='utf-8') as f:
        reader=csv.DictReader(f)

        if reader.fieldnames is None:
            return ValueError("Отсутствуют заголовки в файле")
        dano=list(reader)
    if len(dano)==0:
        return ValueError("Пустой файл")

    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(dano, f, ensure_ascii=False, indent=2)
