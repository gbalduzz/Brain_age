import unittest
import numpy as np
from modules import preprocessing

class PrepTest(unittest.TestCase):
    def test_block_data(self):
        data =np.ones([10,10,10])
        l = [5,5,5]
        blocks = preprocessing.block_data(data, l)
        check = np.ones([2,2,2])*(5**3)
        self.assertTrue((check == blocks).all())
