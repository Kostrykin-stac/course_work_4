import json
from src.vacancy import Vacancy


def test_file_writer():
    vacancy = Vacancy("Ведущий программист-разработчик Unity, C#",
                      "Москва",
                      120000,
                      250000,
                      "Полная занятость",
                      "https://hh.ru/vacancy/93159478")

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancy.__dict__, file, indent=4, ensure_ascii=False)
