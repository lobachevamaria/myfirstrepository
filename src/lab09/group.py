import csv
from pathlib import Path
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создаёт CSV-файл с заголовком, если его нет."""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self):
        "Читает все строки CSV как список словарей."
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != ["fio", "birthdate", "group", "gpa"]:
                raise ValueError("Неверный заголовок CSV-файла")
            for row in reader:
                if not any(row.values()):
                    continue
                rows.append(row)
        return rows

    def _write_all(self, rows):
        "Перезаписывает CSV полностью."
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
    def list(self):
        "Возвращает список Student."
        rows = self._read_all()
        students = []
        for r in rows:
            r2 = {
                "fio": r["fio"],
                "birthdate": r["birthdate"],
                "group": r["group"],
                "gpa": float(r["gpa"])
            }
            students.append(Student.from_dict(r2))
        return students

    def add(self, student: Student):
        "Добавить студента в CSV."
        rows = self._read_all()
        row = student.to_dict()
        row["gpa"] = str(row["gpa"])
        rows.append(row)
        self._write_all(rows)

    def find(self, substr: str):
        "Поиск по подстроке в ФИО (без учета регистра)."
        rows = self._read_all()
        substr = substr.lower()
        found = []
        for r in rows:
            if substr in r["fio"].lower():
                r2 = {
                    "fio": r["fio"],
                    "birthdate": r["birthdate"],
                    "group": r["group"],
                    "gpa": float(r["gpa"])
                }
                found.append(Student.from_dict(r2))
        return found

    def remove(self, fio: str):
        "Удаляет запись по точному ФИО. Возвращает количество удалённых."
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        removed = len(rows) - len(new_rows)

        if removed:
            self._write_all(new_rows)

        return removed
    def update(self, fio: str, **fields):

        rows = self._read_all()

        for r in rows:
            if r["fio"] == fio:
                r.update({k: str(v) for k, v in fields.items()})

        self._write_all(rows)
