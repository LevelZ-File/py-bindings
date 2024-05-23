from .level import Level2D, Level3D
from .block import LevelObject, Block
from .coord import Coordinate2D, Coordinate3D, Dimension

class LevelBuilder:
    """Represents a builder for creating LevelZ Levels."""

    _dimension: Dimension

    _blocks: list[LevelObject] = []

    _headers: dict[str, object] = {}

    def __init__(self, dimension: Dimension):
        """Constructs a LevelBuilder.
        
        :param Dimension dimension: The Dimension of the Level.
        """

        self._dimension = dimension
    
    def add_block(self, block: Block | str, coordinate: Coordinate2D | Coordinate3D | list[int | float]):
        """Adds a Block to the LevelBuilder.
        
        :param block: The Block to add.
        :param coordinate: The Coordinate of the Block.
        """

        if (self._dimension.is2D and not isinstance(coordinate, Coordinate2D)):
            raise ValueError("Coordinate must be 2D for a 2D Level.")
        
        if (self._dimension.is3D and not isinstance(coordinate, Coordinate3D)):
            raise ValueError("Coordinate must be 3D for a 3D Level.")

        self._blocks.append(LevelObject(block, coordinate))
    
    def add_object(self, obj: LevelObject):
        """Adds a LevelObject to the LevelBuilder.
        
        :param LevelObject obj: The LevelObject to add.
        """

        self._blocks.append(obj)
    
    def add_header(self, key: str, value: object):
        """Adds a header to the LevelBuilder.
        
        :param str key: The key of the header.
        :param object value: The value of the header.
        """

        self._headers[key] = value
    
    def build(self):
        """Builds the Level from the LevelBuilder."""
        if (self._dimension.is2D):
            return Level2D(self._headers, self._blocks)
        else:
            return Level3D(self._headers, self._blocks)

    @property
    def dimension(self):
        """Returns the Dimension of the LevelBuilder."""
        return self._dimension

    @property
    def blocks(self):
        """Returns an immutable copy of the blocks in the LevelBuilder."""
        return self._blocks.copy()
    
    @property
    def headers(self):
        """Returns an immutable copy of the headers in the LevelBuilder."""
        return self._headers.copy()

    @staticmethod
    def create_2d():
        """Creates a 2D LevelBuilder."""
        return LevelBuilder(Dimension.TWO)
    
    @staticmethod
    def create_3d():
        """Creates a 3D LevelBuilder."""
        return LevelBuilder(Dimension.THREE)