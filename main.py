from db import people
from application import salary
from datetime import date


def main():
    print('Модуль main выполнен')
    print(f'Текущая дата: {date.today()}')


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    main()
