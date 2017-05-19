import ctypes


class Array1D(object):
    """
    A class-implementation of the 1 dimensional array
    using ctype library.
    """
    def __init__(self, size):
        """
        Creates an array with the given size
        
        :param size: size of the array
        """
        assert size > 0, "Array size must be > 0"  # checks for size > 0
        self._size = size  # sets the argument size to the attribute _size
        array = ctypes.py_object * size  # creates an array with ctypes library and py_object
        self._items = array()  # sets the newly created array to the attribute _items
        self.clear(None)  # clears the array with setting every item to None

    def __len__(self):
        """
        Returns the size of the array.
        
        :return: the size of the array 
        """
        return self._size

    def __getitem__(self, index):
        """
        Returns the value of the element on the given index.
        
        :param index: the index of the element
        :return: value of the element
        """
        assert 0 <= index < self._size, "Invalid index."
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Puts (sets) the value in the array's item
        at the given index position.

        :param index: the index of the element.
        :param value: the value of the element.
        """
        assert 0 <= index < self._size, "Invalid index."
        self._items[index] = value

    def clear(self, value):
        """
        Clears the array by setting each item to the given value.

        :param value: the value to which set each items.
        """
        for i in range(0, len(self)):
            self._items[i] = value

    def __str__(self):
        """
        Converts the adt structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print + ")"

    def __iter__(self):
        """
        Returns the array's iterator for traversing the items.

        :return: the array's iterator for traversing the items. 
        """
        return _ArrayIterator(self._items)


class _ArrayIterator(object):
    """
    An iterator for the Array ADT.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Array2D(object):
    """
    A class-implementation of the Array2D ADT using an array of arrays.
    """
    def __init__(self, num_rows, num_cols):
        """
        Creates a 2D array of size num_rows x num_cols.        
        :param num_rows: number of rows.
        :param num_cols: number of columns.
        """

        # Creates a 1D array to store an array reference for each row.
        self.rows = Array1D(num_rows)

        # Creates the 1D arrays for each row of the 2D array.
        for i in range(num_rows):
            self.rows[i] = Array1D(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2D array.

        :return: the number of rows.
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2D array.

        :return: the number of columns.
        """
        return len(self.rows[0])

    def clear(self, value):
        """
        Clears the array by setting every item to the given value.

        :param value: the value to which set each items.
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]

        :param index_tuple: the index of position. 
        :return: the value.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the item at the position [i,j] to the given value.

        :param index_tuple: the index of position.
        :param value: the value to be set.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            print("row =", row)
            print("col =", col)
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        array_1d[col] = value

    def __str__(self):
        """
        For print() function.
        :return: string to print
        """
        string = "\n"
        for i in range(0, self.num_rows()):
            for j in range(0, self.num_cols()):
                string += str(self[(i, j)]) + " "
            string += "\n"
        return string[1:-1]
