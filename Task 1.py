class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Кол-во страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Кол-во страниц должно быть положительным числом")
        self.__pages = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.__pages})")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self.__duration = float(value)

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.__duration})")