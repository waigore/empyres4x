import unittest

from tests.core.map import *
from tests.core.game import *
from tests.core.player import *
from tests.query import *

def suite():
    mySuite = unittest.TestSuite()
    return mySuite

if __name__ == '__main__':
    unittest.main()
