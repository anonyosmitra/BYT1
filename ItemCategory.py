class ItemCategory:

    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> bool:
        if name is None or name == "":
            return False

        self.__name = name
        return True

    def __str__(self) -> str:
        return self.__name

    def is_valid(self) -> bool:
        return self.__name is not None and self.__name != ""
