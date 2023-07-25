import os
import random
import django
from faker import Faker

# Установка переменной окружения DJANGO_SETTINGS_MODULE для настройки Django.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "search_service.settings")
django.setup()

# Импорт модели Organization из приложения organizations.
from organizations.models import Organization

# Определение функции для генерации фейковых организаций.
def generate_organizations(num):
    # Инициализация объекта Faker с локализацией 'ru_RU' для данных на русском языке.
    fake = Faker('ru_RU')

    # Списки префиксов для полного и сокращенного названия организаций.
    full_names = ['Общество с ограниченной ответственностью', 'Федеральное государственное унитарное предприятие',
                  'Публичное акционерное общество', 'Бюджетное учреждение здравоохранения',
                  'Государственная корпорация', 'Муниципальное унитарное предприятие',
                  'Акционерное общество', 'Министерство здравоохранения', 'Федеральное государственное казенное учреждение',
                  'Администрация губернатора']

    short_names = ['ООО', 'ФГУП', 'ПАО', 'БУЗ', 'ГК', 'МУП', 'АО', 'Минздрав', 'ФГКУ', 'Администрация губернатора']

    # Создание пустого списка для хранения сгенерированных организаций.
    organizations = []

    # Генерация 'num' организаций.
    for i in range(num):
        # Генерация случайного числа для выбора префикса из списков.
        random_number = random.randint(0, 9)

        # Генерация случайного слова и приведение его к верхнему регистру для использования в качестве названия организации.
        random_name = fake.word().capitalize()

        # Объединение префикса, названия организации и кавычек для создания полного и сокращенного названия.
        full_name = full_names[random_number] + ' ' + '«' + random_name + '»'
        short_name = short_names[random_number] + ' ' + '«' + random_name + '»'

        # Генерация случайного 12-значного ИНН (Идентификационный номер налогоплательщика) для организации.
        inn = str(random.randint(100000000000, 999999999999))

        # Создание объекта Organization с сгенерированными данными и добавление его в список.
        organization = Organization(full_name=full_name, short_name=short_name, inn=inn)
        organizations.append(organization)

    # Использование метода bulk_create() Django для эффективной вставки всех организаций в базу данных.
    Organization.objects.bulk_create(organizations)

# Точка входа в скрипт.
if __name__ == "__main__":
    # Запрос у пользователя количества организаций для создания.
    num_organizations = int(input("Введите количество организаций для создания: "))

    # Вызов функции для генерации указанного количества организаций.
    generate_organizations(num_organizations)

    # Вывод сообщения о успешном создании организаций.
    print(f"{num_organizations} организаций успешно созданы.")
