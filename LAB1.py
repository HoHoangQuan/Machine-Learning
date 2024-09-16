import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu chiều cao và cân nặng
X = np.array([180, 162, 183, 174, 160, 163, 180, 165, 175, 170, 170, 169,
              168, 175, 169, 171, 155, 158, 175, 165]).reshape(-1,1)
y = np.array([86, 55, 86.5, 70, 62, 54, 60, 72, 93, 89, 60, 82, 59, 75,
              56, 89, 45, 60, 60, 72]).reshape(-1,1)

# Thêm cột 1 vào X để tính toán hệ số hồi quy
X = np.insert(X, 0, 1, axis=1)

# Tính toán hệ số hồi quy theta bằng công thức (X^T * X)^-1 * X^T * y
X_transpose = X.T
theta = np.linalg.inv(X_transpose @ X) @ X_transpose @ y

# Vẽ đường hồi quy
x1 = 150
y1 = theta[0] + theta[1] * x1
x2 = 190
y2 = theta[0] + theta[1] * x2

plt.plot([x1, x2], [y1, y2], 'r-', label='Đường hồi quy')
plt.plot(X[:,1], y[:,0], 'bo', label='Dữ liệu thực tế')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.title('Chiều cao và cân nặng của sinh viên VLU')
plt.legend()
plt.show()