
def threshold(k,th):
    if k>=th:
        return 1
    else:
        return -1
n=int(input("Enter number of input patterns:"))
x1=[]
x2=[]
t=[]
for i in range(n):
    print("Pattern",i)
    x1.append(int(input("Enter x1:")))
    x2.append(int(input("Enter x2:")))
    t.append(int(input("Enter target:")))
w=[]
w.append(float(input("Enter w1:")))
w.append(float(input("Enter w2:")))
w.append(float(input("Enter bias:")))
lr=float(input("Enter Learning Rate Parameter:"))
th=float(input("Enter Threshold:"))
y=[]
for i in range(n):
    y.append(0)
count=0
while(t!=y):
    count+=1
    if (count>50):
        break
    for i in range(n):
        sum1=0
        sum1+=x1[i]*w[0]+x2[i]*w[1]+w[2]
        y[i]=threshold(sum1, th)
        #e=t[i]-y[i]   for delta rule replace t[i] with e  
        if (y[i]!=t[i]):
            w[0]+=lr*x1[i]*t[i]
            w[1]+=lr*x2[i]*t[i]
            w[2]+=lr*t[i]
        print(w,"iteration", count)
        print(y)
