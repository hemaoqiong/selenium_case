# coding=utf_8
import unittest
from wedget import Wedget


class WidgetTestCase(unittest.TestCase):
    def setup(self):
        self.wedget = Wedget()

    def testSize(self):
        self.assertEquals(self.wedget.getSize(), (40, 40))

    def tearDown(self):
        self.widget = None

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase("testSize"))
        return suite


if __name__ == "__main__":
    unittest.__main__(defaultTest='suite')
