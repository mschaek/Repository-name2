class SocialMedia:
    """
    Базовый класс для социальных сетей.

    Attributes:
        _country (str): Страна происхождения социальной сети.
        _name (str): Название социальной сети.
        _homepage_url (str): URL домашней страницы.

    Инкапсуляция применена для контроля изменения URL и защиты от случайного
    изменения ключевых характеристик (страна, название).
    """

    def __init__(self, country: str, name: str, homepage_url: str):
        """
        Инициализирует объект SocialMedia.

        Args:
            country (str): Страна социальной сети.
            name (str): Название социальной сети.
            homepage_url (str): Адрес домашней страницы.
        """
        self._country = country
        self._name = name
        self._homepage_url = homepage_url

    @property
    def country(self) -> str:
        """Возвращает страну социальной сети."""
        return self._country

    @property
    def name(self) -> str:
        """Возвращает название социальной сети."""
        return self._name

    @property
    def homepage_url(self) -> str:
        """Возвращает URL домашней страницы."""
        return self._homepage_url

    @homepage_url.setter
    def homepage_url(self, new_url: str) -> None:
        """
        Устанавливает новый URL домашней страницы с простой проверкой.

        Args:
            new_url (str): Новый URL.

        Инкапсуляция позволяет контролировать корректность устанавливаемого URL.
        """
        if not new_url:
            raise ValueError("URL не может быть пустым")
        self._homepage_url = new_url

    def get_info(self) -> str:
        """
        Возвращает базовую информацию о социальной сети.

        Returns:
            str: Строка с основными данными.
        """
        return f"{self._name} ({self._country}): {self._homepage_url}"

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление."""
        return (f"Название сайта {self._name}, Страна социальной сети {self._country}, "
                f"Адрес домашней страницы {self._homepage_url}")

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление для воссоздания объекта."""
        return (f"{self.__class__.__name__}(name={self._name!r}, "
                f"country={self._country!r}, homepage_url={self._homepage_url!r})")


class OK(SocialMedia):
    """
    Дочерний класс для социальной сети "Одноклассники" (OK.ru).

    Attributes:
        _five_with_plus (bool): Флаг возможности поставить оценку "5+" фотографии.
    """

    def __init__(self, country: str, name: str, homepage_url: str, five_with_plus: bool):
        """
        Инициализирует объект OK.

        Args:
            country (str): Страна социальной сети.
            name (str): Название социальной сети.
            homepage_url (str): Адрес домашней страницы.
            five_with_plus (bool): Начальное состояние возможности оценки "5+".
        """
        super().__init__(country, name, homepage_url)
        self._five_with_plus = five_with_plus

    @property
    def five_with_plus(self) -> bool:
        """Возвращает текущее состояние флага оценки '5+'."""
        return self._five_with_plus

    def activate_five_plus_rating(self) -> None:
        """
        Активирует возможность ставить оценку "5+" фотографии.

        Метод устанавливает флаг _five_with_plus в True. Предполагается,
        что в реальном приложении здесь могла бы выполняться отправка
        запроса на сервер или изменение настроек пользователя.
        """
        self._five_with_plus = True
        # В реальном коде можно добавить логирование или вызов API

    def get_info(self) -> str:
        """
        Переопределённый метод для расширения информации спецификой OK.

        Возвращает базовую информацию плюс состояние оценки "5+".

        Returns:
           str: Расширенная строка с информацией об OK.
        """
        base_info = super().get_info()
        return f"{base_info}, Оценка 5+: {'доступна' if self._five_with_plus else 'недоступна'}"

    def __str__(self) -> str:
        """
        Перегруженный магический метод для включения информации об оценке.

        Returns:
            str: Строковое представление объекта OK.
        """
        parent_str = super().__str__()
        return f'{parent_str}, Оценка фотографии {self._five_with_plus!r}'