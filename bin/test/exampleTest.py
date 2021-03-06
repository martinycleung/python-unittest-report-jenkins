import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

import xmlrunner
import unittest

from bin import example


class exampleTest(unittest.TestCase):

    def setUp(self):
        self.exampleClass = example.Example()

    def tearDown(self):
        pass

    def testPlusSuccess(self):

        self.assertEqual(self.exampleClass.Plus(1,2),3)

    def testPowerSuccess(self):

        self.assertEqual(self.exampleClass.Power(2,3),8)        
        
    def testDivideSuccess(self):

        self.assertEqual(self.exampleClass.Divide(9,3),3) 
        
    def testMinusSuccess(self):

        self.assertEqual(self.exampleClass.Minus(2, 1), 1)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
