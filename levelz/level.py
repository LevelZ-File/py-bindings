from enum import Enum
from abc import ABC, abstractmethod
from typing import cast

from levelz.block import LevelObject
from levelz.coord import Coordinate2D, Coordinate3D

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

class Level(ABC):
    """Represents a LevelZ level."""

    _dimension: Dimension

    _blocks: set[LevelObject] = set()

    _headers: dict[str, str] = {}

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

        spawn = self._headers.get('spawn')
        if (spawn == None): 
            return None

        if (self._dimension.is2D):
            return Coordinate2D.from_string(spawn)
        else:
            return Coordinate3D.from_string(spawn)
    
class Level2D(Level):
    """Represents a 2D Level."""
    def __init__(self, headers: dict[str, str] = {}, blocks: set[LevelObject] = set()):
        """
        Constructs a 2D Level.

        :param Scroll scroll: The Scroll of the Level.
        :param dict[str, object] headers: The headers of the Level.
        :param set[LevelObject] blocks: The blocks in the Level.
        """
        super().__init__(Dimension.TWO)
        self._headers = headers
        self._blocks = blocks
    
    @property
    def scroll(self):
        """Returns the Scroll of the Level."""
        return self._headers.get('scroll', Scroll.NONE)
    
    @property
    def spawn(self):
        """Returns the spawn point of the Level."""
        return Coordinate2D.from_string(self._headers.get('spawn', "[0, 0]"))

class Level3D(Level):
    """Represents a 3D Level."""
    def __init__(self, headers: dict[str, str] = {}, blocks: set[LevelObject] = set()):
        """
        Constructs a 3D Level.

        :param dict[str, object] headers: The headers of the Level.
        :param set[LevelObject] blocks: The blocks in the Level.
        """
        super().__init__(Dimension.THREE)
        self._headers = headers
        self._blocks = blocks

    @property
    def spawn(self):
        """Returns the spawn point of the Level."""
        return Coordinate3D.from_string(self._headers.get('spawn', "[0, 0, 0]"))