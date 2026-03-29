""" 
Loops

"""

# For Loop

nums = [1,2,3]
for num in nums:
    print(num)

# enumerate() (IMPORTANT)

for index,value in enumerate(nums):
    print(index,value)

# zip() (Used in real projects)
names = ["a", "b"]
ages = [20, 30]

for name,age in zip(names,ages):
    print(name,age)


# DSA - √n logic looping 
# for(int i=0;i*i<=n;i++) equivalent

""" 
math.sqrt(n) → calculates the square root of n
→ Example: if n = 25, result is 5.0
int(math.sqrt(n)) → converts it to an integer
→ 5.0 → 5 (we only need whole numbers for looping)
+ 1 → ensures the loop includes the last value
→ because Python range() excludes the end
range(0, k) → generates numbers from 0 to k-1
So overall, this loop runs from:
→ 0 to √n (inclusive)
This is equivalent to:
→ i * i <= n
Why we do this:
→ Instead of checking till n, we only check till √n → reduces complexity to O(√n)
In short:
→ “Loop only till the square root because anything beyond that is unnecessary work.”

"""

import math
n=5
for i in range(0, int(math.sqrt(n)) + 1):
    pass #  pass means - placeholder, no implementation yet


# While Loop

i=0
while i < 3:
    print(i)
    i+=1


