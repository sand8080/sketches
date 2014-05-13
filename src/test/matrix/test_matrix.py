import unittest2

from matrix import Matrix


class MatrixTestCase(unittest2.TestCase):
    def test_element_not_exist(self):
        m = Matrix(dimensions=(30,))
        self.assertRaises(KeyError, lambda: m[1])
        m = Matrix(dimensions=(10, 3, 4, 5))
        self.assertRaises(KeyError, lambda: m[2][1][0][1])

    def test_correct_element_access(self):
        m = Matrix(dimensions=(30,))
        value = 3
        m[1] = value
        self.assertEquals(value, m[1])

        m = Matrix(dimensions=(10, 3))
        value = 'aa'
        m[4][1] = value
        self.assertEquals(value, m[4][1])

        m = Matrix(dimensions=(10, 3, 4, 5))
        value = 'aa'
        m[0][1][2][3] = value
        self.assertEquals(value, m[0][1][2][3])

    def test_setitem_element_is_not_reached(self):
        m = Matrix(dimensions=(10, 3, 6, 4))
        with self.assertRaises(KeyError):
            m[0] = 'val'
        with self.assertRaises(KeyError):
            m[0][1] = 'val'
        with self.assertRaises(KeyError):
            m[0][1][2] = 'val'

    def test_access_to_item_getitem(self):
        m = Matrix(dimensions=(10,))
        m[0] = ['a', 'b']
        self.assertEquals('b', m[0][1])

    def test_setitem_out_of_bounds(self):
        m = Matrix(dimensions=(10, 3, 4))
        with self.assertRaises(KeyError):
            m[0][2][10] = 'out'

    def test_setitem_out_of_bounds(self):
        m = Matrix(dimensions=(10, 3, 4))
        with self.assertRaises(KeyError):
            m[0][2][10] = 'out'
        m = Matrix(dimensions=(1,))
        with self.assertRaises(KeyError):
            m[1] = 8
