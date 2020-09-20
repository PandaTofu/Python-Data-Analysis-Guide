import numpy as np

np.set_printoptions(suppress=True)

x = np.linspace(0, np.pi, 3)

print("x      = ", x)
print("sin(x) = ", np.sin(x))
print("cos(x) = ", np.cos(x))
print("tan(x) = ", np.tan(x))

x = np.array([30, 45, 60, 90, 180])

print("x      = ", x)
print("sin(x) = ", np.sin(np.radians(x)))
print("cos(x) = ", np.cos(np.radians(x)))
print("tan(x) = ", np.tan(np.radians(x)))

x = np.array([30, 45, 60, 90])

x_r = np.radians(x)

sin_x = np.sin(x_r)

cos_x = np.cos(x_r)

tan_x = np.tan(x_r)

sin_x, cos_x, tan_x

x1 = np.arcsin(sin_x)

x2 = np.arccos(cos_x)

x3 = np.arctan(tan_x)

x1, x2, x3

np.degrees([x1, x2, x3])

