class Box:
    def __init__(self, width: float, length: float, height: float) -> None:
        self.__width = None
        self.__length = None
        self.__height = None

        self.set_width(width)
        self.set_length(length)
        self.set_height(height)

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_length(self) -> float:
        return self.__length

    def set_width(self, width: float) -> None:
        if width <= 0:
            raise ValueError("Width of the box parameters is invalid")

        self.__width = width

    def set_length(self, length: float) -> None:
        if length <= 0:
            raise ValueError("Length of the box parameters is invalid")

        self.__length = length

    def set_height(self, height: float) -> None:
        if height <= 0:
            raise ValueError("Height of the box parameters is invalid")

        self.__height = height

    def volume(self) -> float:
        return self.__width * self.__length * self.__height

    def is_valid(self) -> bool:
        return self.__width > 0 and self.__height > 0 and self.__length > 0
