from abc import ABC, abstractmethod
from levelz.level import Dimension

class Coordinate(ABC):

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

class Coordiante3D(Coordinate):
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