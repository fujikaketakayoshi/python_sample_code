import math
n = 6
nums = [4, 8, 7, 2, 8, 9]
total = sum(nums)

print(round(total/n))  # 四捨五入
print(math.ceil(total/n)) # 小数点以下を切り上げ  
print(math.floor(total/n))  # 小数点以下を切り捨て  
print(int(total/n))  # 小数点以下を切り捨て
print(total//n)  # 小数点以下を切り捨て
print(total/n)  # 小数点以下も表示
