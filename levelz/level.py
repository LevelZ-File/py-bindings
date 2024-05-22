from enum import Enum
from abc import ABCMeta

from levelz.block import LevelObject
from levelz.coord import Dimension, Coordinate2D, Coordinate3D

class Scroll(Enum):
    """Represents the scroll direction of a 2D Level."""

    NONE = 'none'
    """No Scrolling"""

    HORIZONTAL_LEFT = 'horizontal-left'
    """Horizontal Scrolling moving left"""

    HORIZONTAL_RIGHT = 'horizontal-right'
    """Horizontal Scrolling moving right"""

    VERTICAL_UP = 'vertical-up'
    """Vertical Scrolling moving up"""

    VERTICAL_DOWN = 'vertical-down'
    """Vertical Scrolling moving down"""

class Level(metaclass=ABCMeta):
    """Represents a LevelZ level."""

    _dimension: Dimension

    _blocks: list[LevelObject] = []

    _headers: dict[str, object] = {}

    def __init__(self, dimension: Dimension):
        """
        Constructs a Level.

        :param Dimension dimension: The Dimension of the Level.
        """
        self._dimension = dimension
    
    @property
    def dimension(self):
        """Returns the Dimension of the Level."""
        return self._dimension
    
    @property
    def blocks(self):
        """Returns an immutable copy of the blocks in the Level."""
        return self._blocks.copy()
    
    @property
    def headers(self):
        """Returns an immutable copy of the headers in the Level."""
        return self._headers.copy()
    
    @property
    def spawn(self):
        """Returns the spawn point of the Level."""

        spawn = str(self._headers.get('spawn'))
        if (spawn == None): 
            return None

        if (self._dimension.is2D):
            return Coordinate2D.from_string(spawn)
        else:
            return Coordinate3D.from_string(spawn)
    
class Level2D(Level):
    """Represents a 2D Level."""
    def __init__(self, headers: dict[str, object] = {}, blocks: list[LevelObject] = []):
        """
        Constructs a 2D Level.

        :param Scroll scroll: The Scroll of the Level.
        :param dict[str, object] headers: The headers of the Level.
        :param list[LevelObject] blocks: The blocks in the Level.
        """
        super().__init__(Dimension.TWO)
        self._headers = headers
        self._blocks = blocks
    
    @property
    def scroll(self):
        """Returns the Scroll of the Level."""
        s = str(self._headers.get('scroll', "none"))
        return Scroll[s.upper().replace("-", "_")]
    
    @property
    def spawn(self):
        """Returns the spawn point of the Level."""
        return Coordinate2D.from_string(str(self._headers.get('spawn', "[0, 0]")))

class Level3D(Level):
    """Represents a 3D Level."""
    def __init__(self, headers: dict[str, object] = {}, blocks: list[LevelObject] = []):
        """
        Constructs a 3D Level.

        :param dict[str, object] headers: The headers of the Level.
        :param list[LevelObject] blocks: The blocks in the Level.
        """
        super().__init__(Dimension.THREE)

        self._headers = headers
        self._blocks = blocks

    @property
    def spawn(self):
        """Returns the spawn point of the Level."""
        return Coordinate3D.from_string(str(self._headers.get('spawn', "[0, 0, 0]")))