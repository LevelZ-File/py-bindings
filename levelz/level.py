from enum import Enum

class Dimension(Enum):
    """Represents a Game Dimension."""

    TWO = 2
    """Represents a 2D Plane."""

    THREE = 3
    """Represents a 3D Space."""

    def is2D(self):
        """Returns True if the Dimension is 2D."""
        return self == Dimension.TWO
    
    def is3D(self):
        """Returns True if the Dimension is 3D."""
        return self == Dimension.THREE