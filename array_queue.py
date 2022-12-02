# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# from ..exceptions import Empty

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 30          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._first = -1
        self._last = -1

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        # Return (but do not remove) the element at the front of the queue. Raise Empty exception if the queue is empty.
        if self.is_empty():
            #raise Empty('Queue is empty')
            print('fila vazia')
            return None
        else:
            return self._data[self._first]

    def dequeue(self): #desenfileirar
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            print('fila vazia')
            return None  #raise Empty('Queue is empty')
        else:
            answer = self._data[self._first]
            self._data[self._first] = None         # help garbage collection
            if(self._first == self._last):
                self._first = -1
                self._last = -1
            else:
                self._first = (self._first + 1) % len(self._data)
            self._size -= 1
            return answer

    def enqueue(self, e): # enfileirar
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self.data))     # double the array size
        if(self._size == 0):  # fila vazia
            self._data[0] = e
            self._first = 0 # o primeiro elemento esta na posicao zero
            self._last = 0  # o ultimo elemento esta na posicao zero
        else:
            #avail = (self._first + self._size) % len(self._data)
            self._last = (self._last + 1) % len(self._data) # determina a nova posicao do ultimo elemento
            self._data[self._last] = e  # adicona e como ultimo elemento na fila
            #print('avail = {} last = {}'.format(avail, self._last))
            #self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._first
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]            # intentionally shift indices
            walk = (1 + walk) % len(old)         # use old size as modulus
        self._first = 0                        # front has been realigned


