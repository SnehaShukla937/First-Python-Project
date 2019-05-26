import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([7,8,8,9,10,11])

print(a+b)  # add
print(a-b)  # sub
print(a*b)  # prod
print(a/b)  # div
print(a+5)
print(a@b)  # dot prod

z = np.array([22,33,1,2,15,10,88])
x = np.sort(z)  # sort in ascending order
print(x)
c = np.sort(z)[::-1]  # sort in descending order
print(c)