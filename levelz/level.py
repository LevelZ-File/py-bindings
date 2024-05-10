from enum import Enum

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