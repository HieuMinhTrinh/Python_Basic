class SequenceIterator:
    """An iterator for any of Python's sequence types."""
    def __init__ (self, sequence):
        self._seq = sequence
        self._k = -1
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()
        
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
list = [1,2,3,4,5]
test = SequenceIterator(list)
print(test.__next__()) # Result: 1
print("---------------------------------------------------------------------")
#Example: Range Class
"""
There are a few subtleties worth  examining in the code:
+, To properly support optional parameters, we rely on the technique described on page 27, when discussing a functional version of range.
+, We compute the number of elements in range as max(0, (stop - start + step - 1)//step)
+, the __getitem__ method properly supports negative indices by converting an index -k to len(self) -k before computing the result.
"""
class Range:
    """A class that mimic's the built-in range class."""
    def __init__ (self, start, stop = None, step = 1):
        """Initialize a Range instance.
        
        semantics is similar to built-in range class.
        """
        if step==0:
            raise ValueError('Step cannot be 0')
        if stop is None:
            start, stop = 0, start

            #calculate the effective length once
            self._length = max(0,(stop-start+step-1)//step)

            #need knowledge of start and step (but not stop) to support __getitem__
            self._start = start
            self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length
    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k*self._step


# Test
r = Range(100)
for val in r:
    print(r.__getitem__(val))             
