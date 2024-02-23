import json
from src.vacancy import Vacancy, Vacancies
from src.abstracted_classes import JSONABCSaver


class JSONCSaver(Vacancies, JSONABCSaver):
    """
    Сохранение и загрузка данных в формате JSON.
    """

    def save_to_json(self):
        """Сохраняет данные в формате JSON."""
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def load_from_json(self):
        """Загружает данные из файла JSON."""
        try:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                list_dict = json.load(file)
                self._all_vacancies = []
                for item in list_dict:
                    self.all_vacancies.append(Vacancy.from_dict(item))
        except FileNotFoundError:
            print("Файл 'vacancies.json' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла JSON: {e}")
