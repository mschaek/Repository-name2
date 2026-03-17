# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Self


class Table:
    def __init__(self, material: str, length: int) -> None:
        """
        Конструктор класса Table
        :param material: Вид материала из которого сделан стол
        :param length: Длина столешницы
        Пример:
        >>> table = Table("Дерево", 120)
        """
        self.material = material

        if not isinstance(length, int):
            raise TypeError("Параметр длины столешницы должен быть int")

        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

    def move(self, x: float, y: float, z: float) -> None:
        """
        Перемещение стола
        :param x: Перемещение стола по координате x
        :param y: Перемещение стола по координате y
        :param z: Перемещение стола по координате z
        """
        pass

    def craft(self, scheme: dict[str, str]) -> Self:
        """
        Сборка стола по схеме
        :param scheme: Схема сборки
        :return: Новый стол
        """
        pass


class Stone:
    def __init__(self, weight: float, shape: str) -> None:
        """
        Конструктор класса
        :param weight: Вес
        :param shape: Форма
        """
        if weight <= 0:
            raise ValueError("Масса камня должна быть положительным числом")
        self.weight = weight
        self.shape = shape

    def throw(self, distance: int) -> None:
        """
        Функция бросить камень
        :param distance: Дальность броска в метрах
    Пример:
        >>> stone = Stone(25, "Острый")
        >>> stone.throw(25)
        """
        pass

    def explode(self, timer: int) -> bool:
        """
        Взрыв камня
        :param timer: Обратный отсчёт взрыва
        :return: Успешно ли взорван камень
    Пример:
        >>> stone = Stone(25, "Острый")
        >>> stone.explode(5)
        """
        pass


class Builder:
    def __init__(self, education: str, experience: int, last_workplace: str):
        """
        Создание характеристики сотрудника строительнеой компании
        :param education: уровень образования
        :param experience: количество лет работы
        :param last_workplace: последние место работы
        """
        self.education = education
        self.last_workplace = last_workplace

        if experience <= 0:
            raise ValueError("Опыт работы не может быть отрицательным числом")
        self.experience = experience

    def transport(self, speed: int) -> bool:
        """
        Функция перевозки сотрудника
        :param speed: Скорость перевозки
        :return: Успешная перевозка
        """
        if speed <= 0:
            raise ValueError("Скорость транспортировки должна быть положительным числом")
        ...

    def fire(self, reason: str) -> None:
        """
        Функция увольнения сотрудника строительного отдела
        :param reason: Причина увольнения сотрудника строительного отдела
        :return:
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()