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

    def set_width(self, width: float) -> None:
        self.__width = width

    def set_length(self, length: float) -> None:
        self.__length = length

    def set_height(self, height: float) -> None:
        self.__height = height

    def volume(self) -> float:
        return self.__width * self.__length * self.__height
