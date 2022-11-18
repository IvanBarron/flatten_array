import unittest
import main


class TestFlattenArray(unittest.TestCase):
    def test_types(self):
        self.assertRaises(ValueError, main.flatten_array, {"value_1":1, "value_2":2})
        self.assertIsInstance(main.flatten_array([1]), list)

    def test_result(self):
        test_array = [[1,2],3,[4,5,[6,[7,8]],9,[10,11]]]
        self.assertEqual(main.flatten_array(test_array), [1,2,3,4,5,6,7,8,9,10,11])
        test_array_2 = [[1,[2,[3,[4,[5]]]]]]
        self.assertEqual(main.flatten_array(test_array_2), [1,2,3,4,5])
