import numpy as np  # 这一行是召唤 NumPy 库

# 创建一个 2x2 的矩阵 A
A = np.array([[1, 2], [3, 4]]) 
# 创建另一个矩阵 B
B = np.array([[5, 6], [7, 8]])

# 进行矩阵乘法 (点积)
result = np.dot(A, B)
# 矩阵转置
A_transpose = A.T

print("A 的转置结果：")
print(A_transpose)
print("A 乘以 B 的结果：")
print(result)
print("这是矩阵 A：")
print(A)