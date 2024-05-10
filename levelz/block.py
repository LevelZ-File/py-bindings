from levelz.coord import Coordinate

class Block:
    """Represents a Block in a Level."""

    _name: str = ""

    _properties: dict = {}

    def __init__(self, name: str, properties: dict = {}):
        """
        Constructs a Block.

        :param str name: The name of the Block.
        :param dict properties: The properties of the Block.
        """
        self._name = name
        self._properties = properties
    
    @property
    def name(self):
        """Returns the name of the Block."""
        return self._name

    @property
    def properties(self):
        """Returns an immutable copy of the properties for the Block."""
        return self._properties.copy()

    def __str__(self):
        if (len(self._properties) == 0):
            return self._name
        
        s0 = self._name + "<"

        for key, value in self._properties.items():
            s0 += key + "=" + str(value) + ", "
        
        s0 = s0[:-2] + ">"
        return s0

    def __eq__(self, other):
        return self._name == other._name and self._properties == other._properties

class LevelObject:
    """Utility Object for representing a Level Block and its Coordinate."""

    _block: Block

    _coordinate: Coordinate

    def __init__(self, block: Block, coordinate: Coordinate):
        """
        Constructs a LevelObject.

        :param Block block: The Block of the LevelObject.
        :param Coordinate coordinate: The Coordinate of the LevelObject.
        """
        self._block = block
        self._coordinate = coordinate

    @property
    def block(self):
        """Returns the Block of the LevelObject."""
        return self._block
    
    @property
    def coordinate(self):
        """Returns the Coordinate of the LevelObject."""
        return self._coordinate
    
    def __str__(self):
        return f"{self._block}: {self._coordinate}"
    
    def __eq__(self, other):
        return self._block == other._block and self._coordinate == other._coordinate