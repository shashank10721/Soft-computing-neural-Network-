#numpy
import numpy as np
a=np.array([1,2,3,4]) # 1d array
print(a)
print(a.shape) # size of matrix
print(a.size)#total no. of elements
type(a)
b=np.array([[1,2,3],[10,20,30]])
print(b) # 2D matrix

# matrix index from 0 
print(b)
print(b[1,1]) # 2nd row 2 nd colm
print(b[1,:]) # 2nd row
print(b[:,2])# 3rd colum
print(b.sum()) # print sum of elemesnts
print(b.sum(axis=0))# print sum of columns
print(b.sum(axis=1))# print sum of rows
print(np.exp(b))# exponential of matrix
print(np.sqrt(b))# sqrt of b

#zeros matrix
c=np.zeros((3,4)) # 2D zero matrix elements are float
d=np.zeros((3,4),dtype=np.int16) # 2D zero matrix elements are float
e=np.ones((3,4),dtype=np.int16)

#arange function
f=np.arange(10,20,2)# arrange 10 to 19 by step 2
g=np.arange(12).reshape(4,3) # 2d matrix
h=np.arange(24).reshape(4,3,2) # 3d matrix
print(f)print

#linspace
i=np.linspace(10,20,15) # line space 10 to 20 by total 15 points
print(i)

#basicoperations
a=np.array([20,30,40,50])
b=np.arange(4)
print("aray a-b", a-b)
print("aray a+b", a+b)
print("aray a**2", a**2)

# matrix product
a=np.array([[1,1],[0,1]])
b=np.array([[2,0],[3,4]])
print(a*b) # element wise product
print(a.dot(b))# matrix product
print(np.dot(a,b))#matrix product

# random number
a=np.random.random((2,3)) # random no 2 row 3 coloumn

# shape manupulation
b=np.array([[1,2, 3],[4,5,6],[7,8,9],[10,11,12]])
b.reshape(4,3) # converted to 4 x 3 using row wise but orignal matrix unchnaged
b.resize(4,3) #converted to 4 x 3 using row wise but orignal matrix chnaged

## index start from 0
np_height_m = np.array(height) * 0.0254

np_weight_kg = np.array(weight) * 0.453592

bmi = np_weight_kg / np_height_m ** 2 # devide
light=bmi<21 # logical array where bmi<21
print(light)

print(bmi[light])
print (bmi) where bmi<2 

## Array addition & multiplication
print(np_baseball*conversion)
print(np_baseball+conversion)
## basic statistics
# a is vector
np.mean(a)
np.meadian(a)
np.corrcoef(a,b) # correlation of two vectors a and b
np.std(a)
np.sum()
np.sort()
np.round(2.345) =>2 
np.round(2.345,2) =>2.35
h=np.round(np.random.normal(1.75,0.2,5000),2)
w=np.round(np.random.normal(60.3,15,5000),2)# np.random.normal(mean,stdv,number of sample)
np_city=np.column_stack((h,w))
