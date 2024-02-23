class Vacancy:
    """
    Информация о вакансии
    """
    def __init__(self, title, town, salary_from, salary_to, employment, url):
        self.title: str = title
        self.town: str = town
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return (f'Название вакансии: {self.title}\n'
                f'Город: {self.town}\n'
                f'Зарплата от: {self.salary_from}\n'
                f'Зарплата до: {self.salary_to}\n'
                f'Тип занятости: {self.employment}\n'
                f'Ссылка на вакансию: {self.url}\n')

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            'title': self.title,
            'town': self.town,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment': self.employment,
            'url': self.url
        }

    @staticmethod
    def from_dict(vacancy_dict):
        """
        Возвращает вакансию в виде объекта класса Vacancy
        """
        return Vacancy(**vacancy_dict)

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.salary_from < other.salary_from


class Vacancies:
    """ Обработка списка вакансий"""

    def __init__(self):
        self._all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self._all_vacancies.extend(new_vacancies)

    def delete_vacancies(self, old_vacancies):
        for vacancy in old_vacancies:
            self._all_vacancies.remove(vacancy)

    def sort_vacancies_by_salary(self):
        self._all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self._all_vacancies

    def to_list_dict(self):
        """
        Возвращает список вакансий в виде словаря
        """
        return [vacancy.to_dict() for vacancy in self._all_vacancies]
