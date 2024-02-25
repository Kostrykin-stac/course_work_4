from src.utils import user_choice_hh


def user_interaction():
    print('Здравствуйте.\n'
          'Эта программа поможет вам найти вакансии на сайте HeadHunter.\n'
          'Введите "да", чтобы использовать HeadHunter, или "нет", чтобы выйти из программы:')

    while True:
        user_choice_platform = input().lower()
        if user_choice_platform == 'да':
            print('Выбран HeadHunter.')
            user_choice_hh()
            break
        elif user_choice_platform == 'нет':
            print('До свидания!')
            break
        else:
            print('Неверный ввод. Пожалуйста, введите "да" или "нет".')


if __name__ == '__main__':
    user_interaction()
