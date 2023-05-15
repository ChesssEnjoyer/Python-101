Software testing is for testing software product in aspect of expectations of doing the task. It should identify errors, gaps or missing requirements.

##### White Box Testing
- verifing input-output flow
- improving design, usability and security
- code is visible to tester

##### Black Box Testing
- testing functionality of software
- none knowledge about code structure, implementations details and internal paths
- mainly input - output
- based on software requirements and specifications

##### Why?
If there are errors it can be identified early and solved. It saves time and cost effectiveness.
- Cost effectiveness - faster caught bugs = less cost to fix them
- Security - helps remove risks and problems
- Quality of product - tests quality of product before delivering it to the customer
- Satisfaction of custormer - software is written to satisfy customer. Testing ensures best user experience

##### Types of Software Testing:
- Functional Testing:
	- Unit Testing - testing individual unit of code in terms of working properly
	- System testing - testing code as whole, testing functionality, security and portability
	- Smoke
	- User Acceptance Testing (UAT)
	- Localization
	- Globalization
	- Interoperabillity
- Non-Functional Testing:
	- Performance
	- Endurance
	- Load
	- Volume
	- Scalability
	- Usability
- Maintenance:
	- Regression
	- Maintenance



#### 7 Principles of Sotware Testing
- Testing shows presence of defects
- Exhaustive testing is not possible
- Early testing
- Defect clustering
- Pesticide paradox
- Testing is context dependent
- Absence of errors




#### How to write a test plan
- Analyze the product
- Design test strategy
	- Define scope of testing
	- Identify testing type
		![[testmanagement_article_2_4_7 1.webp]]
	- Document risks and issues
	- Create test logistics
		- Who will test?
		- When will test?

- Define test objectives
- Define test criteria
- Resource planning
- Plan test enviroment
- Schedule + estimation
- Determine test deliverables

#### How to write test case:
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