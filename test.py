import math

a = [[1], [2], [3], [4], [5], [6], [7], [1], [2], [3], [4], [5], [6], [7]]
n = math.ceil(len(a) / 4)
nums = []
for i in range(n):
    nums.append([])
k = 0
for i in range(len(a)):
    nums[k].append(a[i])
    if (i+1) % 4 == 0:
        k += 1
print(nums)
print(n)
