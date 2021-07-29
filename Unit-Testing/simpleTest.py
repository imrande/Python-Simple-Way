import unittest


class testDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method')

    def test(self):
        print('Test going here')

    def test2(self):
        print('Test2 going here')

    def tearDown(self):
        print('tearDown method')


if __name__ == '__main__':
    unittest.main()

'''
Answer ==>
setUp method
Test going here
tearDown method
.setUp method
Test2 going here
tearDown method
'''
