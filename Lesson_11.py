# Example: Multidimensional Vector Class
# Behaviors includes the following:
"""
v = Vector(5) => construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23 => <0, 23, 0, 0, 0> (based on use of __setitem__ )
v[-1] = 45 => <0, 23, 0, 0, 45> (also via __setitem__ )
print(v[4]) => print 45 (via __getitem__ )
u=v+v => <0, 46, 0, 0, 90> (via __add__ )
print(u) => print <0, 46, 0, 0, 90>
total = 0
for entry in v: => implicit iteration via __len__ and __getitem__
    total += entry
"""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d # List

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of the vector"""
        return self._coords[j]
    
    def __setitem__ (self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):                     # relies on __len__ method                 # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other                        # rely on existing __eq__ definition
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' # giải thích tại sao là [1:-1] bởi vì sau khi convert sang str là [0, 26, 0, 0, 0]
                                                   # thì str[0] = [ ; str[1] = 0 ; str[2] = , etc..
# Main
v = Vector(5)
v[1] = 13
v[-1] = 45
u = v + v
print(u)
total = 0
for entry in v:
    # print(f"{entry} - {total}")
    total += entry

print(total)