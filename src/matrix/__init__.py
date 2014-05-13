class Matrix(object):
    """Matrix data structure implementation
    Getting element m[j][j]...[k]
    Setting element m[j][j]...[k] = value
    """

    class MatrixElementProxy(object):
        """Matrix proxy element for handling access construction [i][j]...[k]
        """
        def __init__(self, matrix):
            self.matrix = matrix
            self.indexes = []

        def _add_key(self, key):
            self.indexes.append(key)
            # Checking boundary conditions
            indexes_len = len(self.indexes)
            if key >= self.matrix._dimensions[indexes_len - 1]:
                raise KeyError("Key %s is out of bound" % self.get_pretty_matrix_key())

        def __getitem__(self, key):
            self.indexes.append(key)
            if len(self.indexes) == len(self.matrix._dimensions):
                try:
                    return self.matrix._storage[self.get_matrix_key()]
                except KeyError:
                    raise KeyError(self.get_pretty_matrix_key())
            else:
                return self

        def __setitem__(self, key, value):
            self._add_key(key)
            if len(self.indexes) == len(self.matrix._dimensions):
                self.matrix._storage.__setitem__(self.get_matrix_key(), value)
            else:
                raise KeyError("Accessing by key %s is not reaches matrix element" %
                               self.get_pretty_matrix_key())

        def get_pretty_matrix_key(self):
            return '[%s]' % ']['.join(map(str, self.indexes))

        def get_matrix_key(self):
            return tuple(self.indexes)

    def __init__(self, dimensions):
        """Matrix constructor
        :param dimensions: tuple of the Matrix dimension sizes.
        Dimensions (2, 3) means Matrix with 2 columns and 3 rows
        """
        self._storage = dict()
        self._dimensions = dimensions

    def __getitem__(self, key):
        return self.MatrixElementProxy(self).__getitem__(key)

    def __setitem__(self, key, value):
        self.MatrixElementProxy(self).__setitem__(key, value)
