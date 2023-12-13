class Box:

    def __init__(self, width: float, length: float, height: float) -> None:
        self.__width = width
        self.__length = length
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_length(self) -> float:
        return self.__length

    def set_width(self, width: float) -> bool:
        if width <= 0:
            return False

        self.__width = width
        return True

    def set_length(self, length: float) -> bool:
        if length <= 0:
            return False

        self.__length = length
        return True

    def set_height(self, height: float) -> bool:
        if height <= 0:
            return False

        self.__height = height
        return True

    def volume(self) -> float:
        return self.__width * self.__length * self.__height

    def is_valid(self) -> bool:
        return self.__width > 0 and self.__height > 0 and self.__length > 0
