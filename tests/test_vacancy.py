import pytest
from src.vacancy import Vacancy


@pytest.fixture
def v():
    v = Vacancy(
        "Ведущий программист-разработчик Unity, C#",
        "Москва",
        120000,
        250000,
        "Полная занятость",
        "https://hh.ru/vacancy/93159478"
    )
    return v


def test__init__(v):
    assert v.title == "Ведущий программист-разработчик Unity, C#"
    assert v.town == "Москва"
    assert v.salary_from == 120000
    assert v.salary_to == 250000
    assert v.employment == "Полная занятость"  # Corrected attribute name
    assert v.url == "https://hh.ru/vacancy/93159478"