from django.db import models

# Класс модели для представления организации.
class Organization(models.Model):
    """Класс модели организации"""

    # Полное название организации (максимальная длина - 255 символов).
    full_name = models.CharField(max_length=255)

    # Сокращенное название организации (максимальная длина - 100 символов).
    short_name = models.CharField(max_length=100)

    # ИНН (Идентификационный номер налогоплательщика) организации (максимальная длина - 12 символов).
    inn = models.CharField(max_length=12)

    def __str__(self):
        # Метод для представления объекта модели в виде строки (в данном случае, используется полное название).
        return self.full_name

    class Meta:
        # Определение метаданных модели.
        # app_label указывает, к какому приложению относится модель (в данном случае, 'organizations').
        app_label = 'organizations'

