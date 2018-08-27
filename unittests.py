import unittest, random

class TestSort(unittest.TestCase):
    def setUp(self):
        """Setting up a List"""
        self.myList = [random.randint(0,100) for i in range(20)]

    def testLength(self):
        """Tests if the List has the same size after sorting it"""
        lenUnsorted = len(self.myList)
        self.myList.sort()
        lenSorted = len(self.myList)

        self.assertTrue(lenSorted == lenUnsorted)

    def testMin(self):
        """Tests if the min of the List is at the Beginning of the List after sorting"""
        
        minimum = min(self.myList) 
        self.myList.sort()
        self.assertTrue(minimum == self.myList[0])

    def testIsSorted(self):
        """Tests if the sorted List is sorted"""
        self.myList.sort()
        for i in range(0, len(self.myList)-1):
            self.assertFalse(self.myList[i] > self.myList[i+1])

suite = unittest.TestSuite()
suite.addTests((TestSort("testLength"), TestSort("testMin"), TestSort("testIsSorted")))
testrunner = unittest.TextTestRunner(verbosity=1)
testrunner.run(suite)