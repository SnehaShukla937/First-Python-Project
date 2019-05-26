import numpy as np

# make zeros array
z = np.zeros(5)
print(z.shape)
print(z)
z.shape = (5,1) # make different shape
print(z)

x = np.zeros(5,dtype = int)
print(x)

# make ones array
y = np.ones(4,dtype=int)
print(y)
y.shape =(2,2)
print(y)

# make empty(0) array
q = np.empty(8,dtype= int)
print(q)

# linspace from 2 to 10 with 5 elements
p1 = np.linspace(2,10,5)
p2 = np.linspace(5,15,3)
print(p1,p2)

# matrix (array) creation
a = np.array([2,6,8,9])
a.shape = (2,2)
print(a)

values = [3,44,5,5,8,99]
b = np.array([values])
b.shape = (2,3)
print(b)

# random no. generation
r = np.random.randint(10,size=6)
print(r)
print(r[5])
print(r[0])

# array operations
x = np.array([21,22,33])
y = np.where(x>22)
print(y)
print(x>3)
print(x>23)
