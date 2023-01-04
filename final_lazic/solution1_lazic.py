nums = range(100001)
#changing the value to 100000 outputs the answer of 4999950000. I assume counting
#error or something, changing it to 100001 returns 5000050000 which should be right
total = 0
for i in nums:
    total= total + i
    i = 1 + 1
print('The sum of the values 1-100000 is:', total)
