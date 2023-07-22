import unittest
from blockArray import BlockArray

class TestBlockArray(unittest.TestCase):

    def setUp(self):
        self.block_array = BlockArray(block_size=2)

    def test_append_and_len(self):
        self.assertEqual(len(self.block_array), 0)

        self.block_array.append(1)
        self.assertEqual(len(self.block_array), 1)

        self.block_array.append(2)
        self.assertEqual(len(self.block_array), 2)

    def test_insert(self):
        self.block_array.insert(0, 3)
        self.assertEqual(self.block_array._blocks, [[3]])

        self.block_array.insert(0, 4)
        self.assertEqual(self.block_array._blocks, [[4, 3]])

        self.block_array.insert(1, 5)
        self.assertEqual(self.block_array._blocks, [[4, 5], [3]])

    def test_pop(self):
        self.block_array.append(1)
        self.block_array.append(2)
        self.block_array.pop()
        self.assertEqual(self.block_array._blocks, [[1]])

    def test_delete(self):
        self.block_array.append(1)
        self.block_array.append(2)
        self.block_array.delete(0)
        self.assertEqual(self.block_array._blocks, [[None, 2]])

    def test_remove(self):
        self.block_array.append(1)
        self.block_array.append(2)
        self.block_array.append(3)
        self.block_array.append(4)

        self.block_array.remove(1)
        self.assertEqual(self.block_array._blocks, [[1, 3], [4]])

    def test_erase(self):
        self.block_array.append(1)
        self.block_array.append(2)
        self.block_array.append(3)
        self.block_array.append(4)

        self.block_array.remove(1)
        self.assertEqual(self.block_array._blocks, [[1, 3], [4]])

if __name__ == '__main__':
    unittest.main()
