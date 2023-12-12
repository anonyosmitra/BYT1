class Box:

    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    def get_width(self): return self.__width
    def get_height(self): return self.__height
    def get_length(self): return self.__length
    def set_width(self, width): self.__width = width
    def set_length(self, length): self.__length = length
    def set_height(self, height): self.__height = height
    def volume(self): return self.__width * self.__length * self.__height
