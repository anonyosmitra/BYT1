class ItemCategory:

    def __init__(self, name: str) -> None:
        self.set_name(name)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> bool:
        if name is None or name == "":
            raise Exception("Invalid Name")

        self.__name = name
        return True

    def __str__(self) -> str:
        return self.__name
