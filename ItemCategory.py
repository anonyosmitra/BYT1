class ItemCategory:

    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return self.__name
