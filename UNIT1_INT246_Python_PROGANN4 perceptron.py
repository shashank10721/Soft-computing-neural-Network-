import numpy as np
def perceptron(x):
    if x>=0:
        return 1
    else:
        return -1
# inputs [bias=1,in1,in2]
x=np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
d=np.array([[0],[0],[0],[1]])
# Single Neuron
n=1
lr=0.6
# weight initilize by 0.5 [ bias=0.5, w1=0.5,w2=0.5]
w=np.array([0.5, 0.5, 0.5])
cw=np.array([0,0,0])
[r,c]=x.shape

for i in range(r):
    s=0
    for j in range(c):
        s+=x[i,j]*w[j]
    print(s,end=" ")
    if s>=0:
        y=1
    else:
        y=-1
    if y==d[i]:
        for j in range(c):
            cw[j]=0
    else:
        for j in range(c):
            cw[j]=lr*x[i,j]*y
    print(cw,end=" ")
    w=w+cw
    print()

    
    

    
