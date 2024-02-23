import pytest
from src.vacancy import Vacancy
from abc import ABC
from src.abstracted_classes import GetVacancies
from src.hh_API import HeadHunterAPI


@pytest.fixture
def v():
    v = Vacancy("Ведущий программист-разработчик Unity, C#",
                "Москва",
                120000,
                250000,
                "Полная занятость",
                "https://hh.ru/vacancy/93159478")
    return v


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)