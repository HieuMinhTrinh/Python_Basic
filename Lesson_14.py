class Progression:
    def __init__(self, start = 0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__ (self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__ (self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))

# An arithmetic Progression Class
class ArithmeticProgression(Progression):
    def __init__ (self, increment = 1, start = 0):         
        """Create a new arithmetic progression
        
        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """
        super().__init__(start)                       # initialize base class 
        self._increment = increment
    def _advance(self):                               # override inherited version
        self._current += self._increment


# arith_progress = ArithmeticProgression(4,1)
# arith_progress.print_progression(10)
        
# A Geometric Progression Class
class GeometricProgression(Progression):
    def __init__ (self, base = 2, start = 1):
        """ Create a new geometric progression.

        base    the fixed constant multiplied to each term (default 2)
        start   the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base

# Fibonacci Class
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first = 0, second = 1):
        """ Create a new fibonacci progression

        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first
        
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current         # Chú ý cực kì quan trọng: self._current = self._prev + self._current là nó lấy self._prev ở ngoài hàm _advance chứ KHÔNG phải lấy self._prev = self._current

Fibo_Progress = FibonacciProgression()
Fibo_Progress.print_progression(8)