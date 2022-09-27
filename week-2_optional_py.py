print("======= Request-6 (Optional) =======")
# Request-6 (Optional)
def maxZeros(nums):
    max_length = 0
    for i in range(0, len(nums)):
        length = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                length += 1
            else:
                break
        if length > max_length:
            max_length = length
    return max_length
print(maxZeros([0, 1, 0, 0])) # 2
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])) # 4
print(maxZeros([1, 1, 1, 1, 1])) # 0
print(maxZeros([0, 0, 0, 1, 1])) # 3