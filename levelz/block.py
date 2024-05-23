from .coord import Coordinate, Coordinate2D, Coordinate3D

class Block:
    """Represents a Block in a Level."""

    _name: str = ""

    _properties: dict[str, object] = {}

    def __init__(self, name: str, properties: dict[str, object] = {}):
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
        if (isinstance(other, Block)):
            return self._name == other._name and self._properties == other._properties
        
        if (isinstance(other, str)):
            return self._name == other and len(self._properties) == 0

        return False

class LevelObject:
    """Utility Object for representing a Level Block and its Coordinate."""

    _block: Block

    _coordinate: Coordinate

    def __init__(self, block: Block | str, coordinate: Coordinate | list[int | float]):
        """
        Constructs a LevelObject.

        :param Block block: The Block of the LevelObject.
        :param Coordinate coordinate: The Coordinate of the LevelObject.
        """
        if (isinstance(block, str)):
            block = Block(block)

        self._block = block

        if (isinstance(coordinate, list)):
            if (len(coordinate) == 2):
                coordinate = Coordinate2D(coordinate[0], coordinate[1])
            elif (len(coordinate) == 3):
                coordinate = Coordinate3D(coordinate[0], coordinate[1], coordinate[2])
            else:
                raise ValueError(f"Invalid Coordinate: {coordinate}")

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
        if (isinstance(other, LevelObject)):
            return self._block == other._block and self._coordinate == other._coordinate
        
        return False