from Box import Box
from ItemCategory import ItemCategory


class Item:

    def __init__(self, name: str, cost: float, weight: float, box: Box, category: ItemCategory) -> None:
        self.__name = name
        self.__cost = cost
        self.__weight = weight
        self.__box = box
        self.__category = category

    def get_name(self) -> str:
        return self.__name

    def get_cost(self) -> float:
        return self.__cost

    def get_weight(self) -> float:
        return self.__weight

    def get_box(self) -> Box:
        return self.__box

    def get_category(self) -> ItemCategory:
        return self.__category

    def set_name(self, name: str) -> None:
        if name is None or name == "":
            raise ValueError("Name cannot be empty")

        self.__name = name

    def set_cost(self, cost: float) -> None:
        if cost < 0:
            raise ValueError("Cost cannot be negative")

        self.__cost = cost

    def set_weight(self, weight: float) -> None:
        if weight < 0:
            raise ValueError("Weight cannot be negative")

        self.__weight = weight

    def set_box(self, box: Box) -> None:
        self.__box = box

    def set_category(self, category: ItemCategory) -> None:
        self.__category = category

    def __str__(self):
        return f"Name: {self.__name} of {str(self.__category)} category, Cost: {self.__cost}, Weight: {self.__weight}"
