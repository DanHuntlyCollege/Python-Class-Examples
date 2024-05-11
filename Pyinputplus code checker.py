# Pyinputplus input validation tests

import pyinputplus as pyip


response = pyip.inputMenu(['cat', 'dog', 'moose'],prompt='What animal do you prefer?',numbered=True,limit=3,default='cat')

print(f'your favourite animal is a {response}')
