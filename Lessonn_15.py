from abc import ABCMeta, abstractclassmethod          # need these definitions

class Sequence(metaclass = ABCMeta):
    """Our own version of collections. Sequence abstract base class."""
    @abstractclassmethod
    def __len__(self):
        """Return length of the sequence"""

    @abstractclassmethod
    def __getitem__ (self, j):
        """Return the element at index j of the sequence"""

    def __contains__ (self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    
    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
    

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k+= 1
            return k