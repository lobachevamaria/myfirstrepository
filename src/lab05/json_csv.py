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
json_to_csv("data/samples/test.json","data/out/test_from_json.csv")