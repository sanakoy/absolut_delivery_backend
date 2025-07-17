from enum import Enum


# Перечисление для технического состояния

class TechnicalCondition(Enum):
    WORKING = 'Исправно'
    BROKEN = 'Неисправно'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
