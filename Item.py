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

    def set_name(self, name: str) -> bool:
        if name is None or name == "":
            return False

        self.__name = name
        return True

    def set_cost(self, cost: float) -> bool:
        if cost <= 0:
            return False

        self.__cost = cost
        return True

    def set_weight(self, weight: float) -> bool:
        if weight <= 0:
            return False

        self.__weight = weight
        return True

    def set_box(self, box: Box) -> bool:
        if not box.is_valid():
            return False

        self.__box = box
        return True

    def set_category(self, category: ItemCategory) -> bool:
        if not category.is_valid():
            return False

        self.__category = category
        return True

    def __str__(self):
        return f"Name: {self.__name} of {str(self.__category)} category, Cost: {self.__cost}, Weight: {self.__weight}"
