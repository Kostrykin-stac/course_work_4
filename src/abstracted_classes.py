from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """
    Абстрактный класс для метода получения вакансий.

    Этот абстрактный класс определяет метод get_vacancies, который должен
    быть реализован в подклассах для получения информации о вакансиях.
    """
    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


class JSONABCSaver(ABC):
    """
    Абстрактный класс для записи и чтения вакансий в файл JSON.

    Этот абстрактный класс определяет абстрактные методы file_writer и file_reader,
    которые должны быть реализованы в подклассах для записи и чтения данных в/из файла JSON.
    """
    @abstractmethod
    def file_writer(self):
        pass

    @abstractmethod
    def file_reader(self):
        pass
