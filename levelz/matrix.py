from enum import Enum
from abc import ABCMeta, abstractmethod
import re

from .coord import Dimension, Coordinate2D, Coordinate3D

class CoordinateMatrix(metaclass=ABCMeta):
    """Represents a corodinate matrix."""

    @property
    @abstractmethod
    def dimension(self):
        """Return the dimension of the matrix."""
        pass

    @property
    @abstractmethod
    def coordinates(self):
        """Return the coordinates of the matrix."""
        pass

    @property
    @abstractmethod
    def start(self):
        """Return the starting coordinate for the matrix."""
        pass

class CoordinateMatrix2D(CoordinateMatrix):
    """Represents a 2-Dimensional Coordinate Matrix."""

    minX: int = 0
    """The minimum x-coordinate of the Matrix."""

    maxX: int = 0
    """The maximum x-coordinate of the Matrix."""

    minY: int = 0
    """The minimum y-coordinate of the Matrix."""

    maxY: int = 0
    """The maximum y-coordinate of the Matrix."""

    _start: Coordinate2D

    def __init__(self, minX: int, maxX: int, minY: int, maxY: int, start: Coordinate2D):
        """
        Constructs a 2D Coordinate Matrix.

        :param int minX: The minimum x-coordinate of the Matrix.
        :param int maxX: The maximum x-coordinate of the Matrix.
        :param int minY: The minimum y-coordinate of the Matrix.
        :param int maxY: The maximum y-coordinate of the Matrix.
        :param Coordinate2D start: The starting Coordinate of the Matrix.
        """
        if (minX > maxX):
            raise ValueError("minX must be less than or equal to maxX.")

        if (minY > maxY):
            raise ValueError("minY must be less than or equal to maxY.")

        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self._start = start

    @property
    def dimension(self):
        return Dimension.TWO

    @property
    def coordinates(self):
        coords: list[Coordinate2D] = []

        for x in range(self.minX, self.maxX + 1):
            for y in range(self.minY, self.maxY + 1):
                coords.append(Coordinate2D(x, y))

        return coords
    
    @property
    def start(self):
        return self._start

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __str__(self):
        return f"({self.minX}, {self.maxX}, {self.minY}, {self.maxY})^{self.start}"

    def __eq__(self, other):
        if (isinstance(other, CoordinateMatrix2D)):
            return self.minX == other.minX and self.maxX == other.maxX and self.minY == other.minY and self.maxY == other.maxY and self.start == other.start

        return False

    @staticmethod
    def from_string(string: str):
        """
        Converts a string to a 2D Coordinate Matrix.

        :param str string: The string to convert.
        :return: The 2D Coordinate Matrix.
        :rtype: CoordinateMatrix2D
        """

        split = re.split(r"\^", string)

        coords = re.sub(r"[\[\]\s]", "", split[1]).split(",")
        matrix = re.sub(r"[()\s]", "", split[0]).split(",")

        if (len(coords) != 2): raise ValueError(f"Invalid 2D Coordinate: {string}")
        if (len(matrix) != 4): raise ValueError(f"Invalid 2D Matrix: {string}")

        cx = float(coords[0]); cy = float(coords[1])
        x1 = int(matrix[0]); x2 = int(matrix[1])
        y1 = int(matrix[2]); y2 = int(matrix[3])

        return CoordinateMatrix2D(x1, x2, y1, y2, Coordinate2D(cx, cy))


class CoordinateMatrix3D(CoordinateMatrix):
    """Represents a 3-Dimensional Coordinate Matrix."""

    minX: int = 0
    """The minimum x-coordinate of the Matrix."""

    maxX: int = 0
    """The maximum x-coordinate of the Matrix."""

    minY: int = 0
    """The minimum y-coordinate of the Matrix."""

    maxY: int = 0
    """The maximum y-coordinate of the Matrix."""

    minZ: int = 0
    """The minimum z-coordinate of the Matrix."""

    maxZ: int = 0
    """The maximum z-coordinate of the Matrix."""

    _start: Coordinate3D

    def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, start: Coordinate3D):
        """
        Constructs a 3D Coordinate Matrix.

        :param int minX: The minimum x-coordinate of the Matrix.
        :param int maxX: The maximum x-coordinate of the Matrix.
        :param int minY: The minimum y-coordinate of the Matrix.
        :param int maxY: The maximum y-coordinate of the Matrix.
        :param int minZ: The minimum z-coordinate of the Matrix.
        :param int maxZ: The maximum z-coordinate of the Matrix.
        """
        if (minX > maxX):
            raise ValueError("minX must be less than or equal to maxX.")

        if (minY > maxY):
            raise ValueError("minY must be less than or equal to maxY.")

        if (minZ > maxZ):
            raise ValueError("minZ must be less than or equal to maxZ.")

        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
        self._start = start

    @property
    def dimension(self):
        return Dimension.THREE

    @property
    def coordinates(self):
        coords: list[Coordinate3D] = []

        for x in range(self.minX, self.maxX + 1):
            for y in range(self.minY, self.maxY + 1):
                for z in range(self.minZ, self.maxZ + 1):
                    coords.append(Coordinate3D(x, y, z))

        return coords
    
    @property
    def start(self):
        return self._start

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __str__(self):
        return f"({self.minX}, {self.maxX}, {self.minY}, {self.maxY}, {self.minZ}, {self.maxZ})^{self.start}"

    def __eq__(self, other):
        if (isinstance(other, CoordinateMatrix3D)):
            return self.minX == other.minX and self.maxX == other.maxX and self.minY == other.minY and self.maxY == other.maxY and self.minZ == other.minZ and self.maxZ == other.maxZ and self.start == other.start

        return False
    
    @staticmethod
    def from_string(string: str):
        """
        Converts a string to a 3D Coordinate Matrix.
        
        :param str string: The string to convert.
        :return: The 3D Coordinate Matrix.
        :rtype: CoordinateMatrix3D
        """ 

        split = re.split(r"\^", string)

        coords = re.sub(r"[\[\]\s]", "", split[1]).split(",")
        matrix = re.sub(r"[()\s]", "", split[0]).split(",")

        if (len(coords) != 3): raise ValueError(f"Invalid 3D Coordinate: {string}")
        if (len(matrix) != 6): raise ValueError(f"Invalid 3D Matrix: {string}")

        cx = float(coords[0]); cy = float(coords[1]); cz = float(coords[2])
        x1 = int(matrix[0]); x2 = int(matrix[1])
        y1 = int(matrix[2]); y2 = int(matrix[3])
        z1 = int(matrix[4]); z2 = int(matrix[5])

        return CoordinateMatrix3D(x1, x2, y1, y2, z1, z2, Coordinate3D(cx, cy, cz))
