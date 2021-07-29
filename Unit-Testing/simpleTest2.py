import unittest


class testDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUp method')

    def test(self):
        print('Test going here')

    def test2(self):
        print('Test2 going here')

    @classmethod
    def tearDownClass(cls):
        print('tearDown method')


if __name__ == '__main__':
    unittest.main()

'''
Answer ==>
setUp method
Test going here
.Test2 going here
.tearDown method
'''
