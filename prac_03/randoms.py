""" What did you see on line 1?
On line 1, a random integer between 5 and 20.
What was the smallest number you could have seen, what was the largest?
The smallest number is 5, and the largest is 20.

What did you see on line 2?
On line 2, a random number between 3 and 10 with a step of 2.
What was the smallest number you could have seen, what was the largest?
The smallest number that can be seen is 3, and the largest is 9
Could line 2 have produced a 4?
No.

What did you see on line 3?
On line 3, a random floating-point number between 2.5 and 5.5.
What was the smallest number you could have seen, what was the largest?
The smallest number is infinitely close to 2.5, and the largest is infinitely close to 5.5.
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

import random
random_number = random.randint(1, 100)
print(random_number)