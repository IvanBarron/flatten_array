""" main """

import unittest
import test
from functions import flatten_array

if __name__ == '__main__':
  
  test_array = [[1,2],3,[4,5,[6,[7,8]],9,[10,11]]]
  
  result = flatten_array(test_array)
  print(f"Test Array: {test_array}")
  print(f"Result Array: {result}")
  unittest.main(module=test)
