print("======= Request-4 =======")
# Request-4
def maxProduct(nums):
    for i in range(len(nums), 1, -1):
        flag = 0
        for j in range(0, i-1):
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = 1
        if flag == 0:
            break
    last_index = len(nums) - 1
    if nums[last_index] * nums[last_index-1] > nums[0] * nums[1]:
        return nums[last_index] * nums[last_index-1]
    else:
        return nums[0] * nums[1]
print(maxProduct([5, 20, 2, 6])) # 得到 120
print(maxProduct([10, -20, 0, 3])) # 得到 30
print(maxProduct([10, -20, 0, -3])) # 得到 60
print(maxProduct([-1, 2])) # 得到 -2
print(maxProduct([-1, 0, 2])) # 得到 0
print(maxProduct([5,-1, -2, 0])) # 得到 2
print(maxProduct([-5, -2])) # 得到 10

print("======= Request-5 =======")
# Request-5
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.
def twoSum(nums, target):
    dic = {} # dictionary
    for i in range(0, len(nums)):
        if str(target-nums[i]) in dic: # str(): change integer to string 
            return [dic[str(target-nums[i])], i] # get value from key "target-nums[i]"
        else:
            dic[str(nums[i])] = i # store nums[i] as key, i as value
result = twoSum([2, 11, 7, 15], 9)
print(result)
