print("======= Request-1 =======")
# Reuest-1
def calculate(min, max, step):
    sum = 0
    i=min
    while i <= max:
        sum += i
        i += step
    return sum
print(calculate(1,3,1)) # 你的程式要能夠計算 1+2+3，最後印出 6
print(calculate(4,8,2)) # 你的程式要能夠計算 4+6+8，最後印出 18
print(calculate(-1,2,2)) # 你的程式要能夠計算 -1+1，最後印出 0

print("======= Request-2 =======")
# Request-2
def avg(data):
    sum = 0
    n = 0
    for i in range(0, len(data["employees"])):
        if data["employees"][i]["manager"] == False:
            sum += data["employees"][i]["salary"]
            n += 1 # 計算非 manager 的員工數量
    return sum / n
print(avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}))

print("======= Request-3 =======")
# Request-3
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
def func(a):
    def result(b, c):
        return a + (b * c)
    return result
print(func(2)(3, 4)) # 2+(3*4) = 14
print(func(5)(1, -5)) # 5+(1*-5) = 0
print(func(-3)(2, 9)) # -3+(2*9) = 15

print("======= Request-4 =======")
# Request-4
def maxProduct(nums):
    max = nums[0]*nums[1]
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > max:
                max = nums[i] * nums[j]
    return max
print(maxProduct([5, 20, 2, 6])) # 得到 120
print(maxProduct([10, -20, 0, 3])) # 得到 30
print(maxProduct([10, -20, 0, -3])) # 得到 60
print(maxProduct([-1, 2])) # 得到 -2
print(maxProduct([-1, 0, 2])) # 得到 0
print(maxProduct([5,-1, -2, 0])) # 得到 2
print(maxProduct([-5, -2])) # 得到 10

print("======= Request-5 =======")
# Request-5
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums [j] == target:
                result = [i, j]
                break
    return result
result = twoSum([2, 11, 7, 15], 9)
print(result)