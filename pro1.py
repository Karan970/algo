import numpy as np
a = input("Enter List A").split()
a = list(map(int,a))
b = a = input("Enter List B").split()
b = list(map(int,b))
A = np.array(a)
print(A*A)