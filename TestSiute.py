import unittest
import creatingNewUsers, deletingAutoTestUser

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.makeSuite(creatingNewUsers.TestCreation))
testSuite.addTest(unittest.makeSuite(deletingAutoTestUser.DeletingTestUser))

suite = unittest.TextTestRunner(verbosity = 2)
suite.run(testSuite)
