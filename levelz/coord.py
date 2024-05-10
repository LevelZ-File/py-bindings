from abc import ABC, abstractmethod
from levelz.level import Dimension

class Coordinate(ABC):
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
        return self.x == other.x and self.y == other.y

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
        return self.x == other.x and self.y == other.y and self.z == other.z
    
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