"""Онлайн-дневник студента с расписанием занятий (консольная версия)."""
import json
from pathlib import Path

DATA_FILE = Path("diary_data.json")
DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]


def load():
    """Загрузить данные дневника из файла."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {"schedule": {d: [] for d in DAYS}, "homework": [], "grades": {}}


def save(data):
    """Сохранить данные дневника в файл."""
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                         encoding="utf-8")


def add_lesson(data, day, time, subject):
    """Добавить занятие в расписание дня."""
    data["schedule"][day].append({"time": time, "subject": subject})
    data["schedule"][day].sort(key=lambda lesson: lesson["time"])


def add_homework(data, subject, task, deadline):
    """Записать домашнее задание со сроком сдачи."""
    data["homework"].append(
        {"subject": subject, "task": task, "deadline": deadline})


def add_grade(data, subject, grade):
    """Добавить оценку (от 2 до 5) по предмету."""
    if grade not in (2, 3, 4, 5):
        raise ValueError("Оценка должна быть от 2 до 5")
    data["grades"].setdefault(subject, []).append(grade)


def average(data, subject):
    """Средний балл по предмету (None, если оценок нет)."""
    grades = data["grades"].get(subject, [])
    return round(sum(grades) / len(grades), 2) if grades else None


def show_schedule(data):
    for day in DAYS:
        print(day + ":")
        for lesson in data["schedule"][day]:
            print("  {time}  {subject}".format(**lesson))


def main():
    data = load()
    while True:
        print("\n1 - Расписание  2 - Новое занятие  3 - Домашнее задание")
        print("4 - Оценка  5 - Средний балл  0 - Выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            show_schedule(data)
        elif choice == "2":
            add_lesson(data, input("День: "), input("Время (ЧЧ:ММ): "),
                       input("Предмет: "))
        elif choice == "3":
            add_homework(data, input("Предмет: "), input("Задание: "),
                         input("Срок сдачи: "))
        elif choice == "4":
            add_grade(data, input("Предмет: "), int(input("Оценка: ")))
        elif choice == "5":
            subject = input("Предмет: ")
            print("Средний балл:", average(data, subject))
        elif choice == "0":
            save(data)
            break


if __name__ == "__main__":
    main()
