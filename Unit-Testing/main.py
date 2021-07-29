'''
2 types of testing
1) Unit testing
-> Process of testing
whether the particular unit is working or not, the process is called Unit testing
2) Integraton testing (End to end Testing)
-> The process of total application testing is called Integraton testing [it's QA Team job]

difference between test Scenario, test case, test suite =>
test Scenario
-> username login funcationality [Gmail]
testCase
->
1. valid username check
2. invalid username check
3. empty username
4.
test suite
একটা test Scenario এর possible test case গুলোে একত্র করে যে test করা হয় তাকে test suite বলে, it checks all testcase
-> combine all test case together and then test one single file is called test suite

Unittest in python =>
Module name: unittest
class Name: testCases
Instance Methods: 3 Methods
1. setUp()
2. test()
3. tearDown()
class Methods:
1. tearDownClass(cls)
-> If any test case tearDown() is same then we can use tearDownClass(cls) method
2. setUpClass(cls)
-> If any test case setUp() is same then we can use setUpClass(cls) method

Automation testing ==> Selenium, QTP, load runner(performance testing tool)
'''
