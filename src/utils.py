from src.hh_API import HeadHunterAPI
from src.jsonsaver import JSONCSaver


def user_choice_hh():
    # Запрашиваем у пользователя название профессии
    profession_keyword = input('Введите название профессии: \n')

    # Создаем экземпляр класса HeadHunterAPI для работы с API HeadHunter
    hh_api = HeadHunterAPI()

    # Запрашиваем у пользователя количество страниц для вывода
    print('Сколько страниц вывести? \n')
    number_of_pages = int(input())

    # Получаем список вакансий с сайта HeadHunter
    vacancies_from_hh = hh_api.get_vacancies(profession_keyword, number_of_pages)

    # Печатаем список вакансий после того, как он был получен
    print('Список вакансий с сайта "HeadHunter": \n')
    for vacancy in vacancies_from_hh:
        print(vacancy)

    # Запрашиваем у пользователя желание сохранить данные в JSON файл
    print('Записать данные, отсортированные по зарплате, в JSON файл? ')
    user_answer = input('Да\Нет \n').lower()

    # Если пользователь отказался от сохранения, выводим сообщение об этом
    if user_answer not in ['да']:
        print('Спасибо за использование программы')
    else:
        # Создаем экземпляр класса JSONCSaver для сохранения данных в JSON файл
        jsonfile_hh = JSONCSaver()
        jsonfile_hh.add_vacancies(vacancies_from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()

        # Возвращаем созданный экземпляр класса JSONCSaver для возможного дальнейшего использования
        return jsonfile_hh


