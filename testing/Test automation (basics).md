Automation testing is about automating application testing process.
##### Benefits:
- It saves cost
- It's faster and more accurate than manual testing
- It's more effective by allowing to detect bugs way faster
##### Criteria:
Test that should be automated:
- Repetitive and time-consuming tests
- Tests for multiple builds
- Tests vunerable to human error
- High-risk tests
- Tests which can't be done manually
- Tests that needs to be run on multiple software

##### Types:
 - Unit test - testing small part of software in terms of functionality
 - Smoke test - stable of particular build
 - Integration test - testing if software works together as whole
 - Regression test - testing functional and non-functional parts, checks if sotware component has regressed after changes
 - Security test - checks functional nad non-functional parts, tests security of application
 - Performance test - non-functional test, checks how stable and responsible application is
 - API test - tests if software performs as it should with other systems
 - UI test - tests final version performs as it should during user interaction

 ##### Process
1. Select tool - depends on:
	- what language is software written in
	- what are testinf requirements
2. Define the scope
3. Plan, design and develop
4. Execute the test
5. Maintance

##### How to write test case:
File name: test_plik.py
```
import unittest
import calc

class Test(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(10,5), 15)
		self.assertEqual(calc.add(1,-1), 0)
		self.assertEqual(calc.add(-1,-1), -2)


```

Running test:
```
python -m unittest test_plik.py
```
	If we add that at the end:
```
if __name__ == '__main__':
	unittest.main()
```

```
python3 test_plik.py
```