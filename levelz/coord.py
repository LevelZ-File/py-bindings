from enum import Enum
from abc import ABCMeta, abstractmethod

class Dimension(Enum):
    """Represents a Game Dimension."""

    TWO = 2
    """Represents a 2D Plane."""

    THREE = 3
    """Represents a 3D Space."""

    @property
    def is2D(self):
        """Returns True if the Dimension is 2D."""
        return self == Dimension.TWO
    
    @property
    def is3D(self):
        """Returns True if the Dimension is 3D."""
        return self == Dimension.THREE

    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        if (isinstance(other, Dimension)):
            return self.value == other.value

        if (isinstance(other, int)):
            return self.value == other
        
        if (isinstance(other, str)):
            return self.value == int(other)

        return False

class Coordinate(metaclass=ABCMeta):
    """Represents a Game Coordinate."""

    @property
    @abstractmethod
    def magnitude(self):
        """Return the magnitude of the coordinate."""
        pass

    @property
    @abstractmethod
    def dimension(self):
        """Return the dimension of the coordinate."""
        pass

class Coordinate2D(Coordinate):
    """Represents a 2-Dimensional Coordinate."""

    x: float = 0
    """The x-coordinate of the 2D Coordinate."""

    y: float = 0
    """The y-coordinate of the 2D Coordinate."""
    
    def __init__(self, x: float, y: float):
        """
        Constructs a 2D Coordinate.

        :param float x: The x-coordinate of the 2D Coordinate.
        :param float y: The y-coordinate of the 2D Coordinate.
        """
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def dimension(self):
        return Dimension.TWO

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __eq__(self, other):
        if (isinstance(other, Coordinate2D)):
            return self.x == other.x and self.y == other.y
        
        if (isinstance(other, list)):
            return self.x == other[0] and self.y == other[1]
        
        if (isinstance(other, tuple)):
            return self.x == other[0] and self.y == other[1]

        if (isinstance(other, str)):
            return self == Coordinate2D.from_string(other)

        return False

    @staticmethod
    def from_string(s: str):
        """
        Parses a string to create a 2D Coordinate.

        :param str s: The string to parse.
        :return: The 2D Coordinate.
        :rtype: Coordinate2D
        """
        s0 = s.strip()
        s1 = s0[1:-1].split(",")
        x = float(s1[0].strip())
        y = float(s1[1].strip())
        return Coordinate2D(x, y)

class Coordinate3D(Coordinate):
    """Represents a 3-Dimensional Coordinate."""

    x: float = 0
    """The x-coordinate of the 3D Coordinate."""

    y: float = 0
    """The y-coordinate of the 3D Coordinate."""

    z: float = 0
    """The z-coordinate of the 3D Coordinate."""
    
    def __init__(self, x: float, y: float, z: float):
        """
        Constructs a 3D Coordinate.
        
        :param float x: The x-coordinate of the 3D Coordinate.
        :param float y: The y-coordinate of the 3D Coordinate.
        :param float z: The z-coordinate of the 3D Coordinate.
        """
        self.x = x
        self.y = y
        self.z = z

    @property
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    @property
    def dimension(self):
        return Dimension.THREE

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def __eq__(self, other):
        if (isinstance(other, Coordinate3D)):
            return self.x == other.x and self.y == other.y and self.z == other.z
        
        if (isinstance(other, list)):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        
        if (isinstance(other, tuple)):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]

        if (isinstance(other, str)):
            return self == Coordinate3D.from_string(other)

        return False
    
    @staticmethod
    def from_string(s: str):
        """
        Parses a string to create a 3D Coordinate.

        :param str s: The string to parse.
        :return: The 3D Coordinate.
        :rtype: Coordiante3D
        """
        s0 = s.strip()
        s1 = s0[1:-1].split(",")
        x = float(s1[0].strip())
        y = float(s1[1].strip())
        z = float(s1[2].strip())
        return Coordinate3D(x, y, z)