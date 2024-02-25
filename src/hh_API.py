import requests
from src.vacancy import Vacancy
from src.abstracted_classes import GetVacancies


class HeadHunterAPI(GetVacancies):
    """Класс для подключения к сайту hh.ru"""

    def get_vacancies(self, name_job, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        hh_list = []
        for i in range(pages):
            params = {
                'text': name_job,
                'per_page': 99,
                'page': i
            }
            try:
                response = requests.get('https://api.hh.ru/vacancies', params=params)
                response.raise_for_status()  # Проверка на успешный запрос
                response_json = response.json()
                for j in response_json.get('items', []):  # Проверка наличия ключа 'items'
                    hh_title = j.get('name', 'Unknown')  # Проверка наличия ключа 'name'
                    hh_town = j.get('area', {}).get('name')  # Проверка наличия ключа 'area'
                    salary_info = j.get('salary', {})
                    salary_from = salary_info.get('from', 0) if salary_info else 0  # Проверка наличия ключа 'from'
                    salary_to = salary_info.get('to', 0) if salary_info else 0  # Проверка наличия ключа 'to'
                    hh_employment = j.get('employment', {}).get('name')  # Проверка наличия ключа 'employment'
                    hh_url = j.get('alternate_url', 'Unknown')  # Проверка наличия ключа 'alternate_url'
                    hh_vacancy = Vacancy(hh_title, hh_town, salary_from, salary_to, hh_employment, hh_url)
                    hh_list.append(hh_vacancy)
            except requests.RequestException as e:
                print(f"Произошла ошибка при запросе к API HeadHunter: {e}")
                # Продолжение выполнения цикла или возврат пустого списка
                continue
            except Exception as e:
                print(f"Произошла ошибка при обработке данных: {e}")
        return hh_list
