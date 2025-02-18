class Electronics:
    """
    Базовый класс для электроники.

    Атрибуты:
        brand (str): Бренд электроники.
        model (str): Модель электроники.
        price (float): Цена электроники.
    """

    def __init__(self, brand: str, model: str, price: float) -> None:
        """
        Инициализация базового класса Electronics.

        Аргументы:
            brand (str): Бренд электроники.
            model (str): Модель электроники.
            price (float): Цена электроники.
        """
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self) -> str:
        """Возвращает строку с информацией об устройстве."""
        return f"{self.brand} {self.model} - {self.price} руб."

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"Electronics(brand='{self.brand}', model='{self.model}', price={self.price})"

    def power_on(self) -> None:
        """Включает устройство."""
        print(f"{self.brand} {self.model} включен.")


class Smartphone(Electronics):
    """
    Класс, представляющий смартфон.

    Атрибуты:
        os (str): Операционная система смартфона.
    """

    def __init__(self, brand: str, model: str, price: float, os: str) -> None:
        """
        Инициализация класса Smartphone, наследованного от Electronics.

        Аргументы:
            brand (str): Бренд смартфона.
            model (str): Модель смартфона.
            price (float): Цена смартфона.
            os (str): Операционная система смартфона.
        """
        super().__init__(brand, model, price)
        self.__os = os  # Приватный атрибут, так как он не должен быть доступен извне.

    def __str__(self) -> str:
        """Возвращает строку с информацией о смартфоне."""
        return f"{self.brand} {self.model} - {self.price} руб. (OS: {self.__os})"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"Smartphone(brand='{self.brand}', model='{self.model}', price={self.price}, os='{self.__os}')"

    def power_on(self) -> None:
        """Включает смартфон и показывает информацию о системе.

        Переопределённый метод, который добавляет вывод информации о системе
        вместе с включением устройства.
        """
        super().power_on()
        print(f"Операционная система: {self.__os}")


class Laptop(Electronics):
    """
    Класс, представляющий ноутбук.

    Атрибуты:
        ram (int): Объем оперативной памяти в ГБ.
    """

    def __init__(self, brand: str, model: str, price: float, ram: int) -> None:
        """
        Инициализация класса Laptop, наследованного от Electronics.

        Аргументы:
            brand (str): Бренд ноутбука.
            model (str): Модель ноутбука.
            price (float): Цена ноутбука.
            ram (int): Объем оперативной памяти в ГБ.
        """
        super().__init__(brand, model, price)
        self.ram = ram

    def __str__(self) -> str:
        """Возвращает строку с информацией о ноутбуке."""
        return f"{self.brand} {self.model} - {self.price} руб. (RAM: {self.ram} ГБ)"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"Laptop(brand='{self.brand}', model='{self.model}', price={self.price}, ram={self.ram})"

    def power_on(self) -> None:
        """Включает ноутбук и показавает информацию о памяти."""
        super().power_on()
        print(f"Объем оперативной памяти: {self.ram} ГБ")