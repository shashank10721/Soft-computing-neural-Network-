import random
import math
def objective(m):#Objective Function
    return(abs((m[0]+2*m[1]+3*m[2]+4*m[3])-30))
def fitness(m): #Fitness Function
    return(1/(1+m))
def probability(m,n): #Probability Function
    return(m/n)
def crossover(m,n): #Crossover
    pt=random.randint(0,3)
    return(m[:pt+1]+n[pt+1:])
print("Minimize a+2b+3c+4d-30")
print("Population size: 6")
pop1=[]
#Initialize random population
for i in range(6):
    pop1.append([])
    for j in range(4):
        pop1[i].append(random.randint(0,30))
print("Initial Populaion: ")
for i in range(6):
    print(pop1[i])
#Maximum iterations 10
for it in range(10):
    obj=[0]*6
    print("Objective Function: ")
    for i in range(6):
        obj[i]=objective(pop1[i])
        print(obj[i])
    fit=[0]*6
    print("Fitness Value: ")
    for i in range(6):
        fit[i]=fitness(obj[i])
        print(fit[i])
    print("Total fitness: ",sum(fit))
    prob=[0]*6
    #Probability calculation
    for i in range(6):
        prob[i]=probability(fit[i],sum(fit))
    #Commulative Probability Calculation
    cmp=[0]*6
    sum1=0
    for i in range(6):
        sum1+=prob[i]
        cmp[i]=sum1
    #Roulette Wheel Selection
    R=[0]*6
    
    for i in range(6):
        R[i]=random.random()
    new_pop=[]
    
    for i in range(6):
        for j in range(6):
            if R[i]<=cmp[j]:
                new_pop.append(pop1[j])
                break
    
    print("After Selection: ",new_pop)
    #Crossover
    cr=0.25#Crossover Rate
    CR=[0]*6
    for i in range(6):
        CR[i]=random.random()
    par=[]
    par_index=[]
    
    for i in range(6):
        if CR[i]<cr:
            par.append(new_pop[i])
            par_index.append(i)
    
    x=len(par)
    for i in range(x):
        a=random.randint(0,x-1)
        b=random.randint(0,x-1)
        new_pop[par_index[i]]=crossover(par[a],par[b])
    #Mutation
    mr=0.1 #mutation rate
    total_mut=math.floor(24*mr)
    mut_index=[]
    mut_value=[]
    for i in range(total_mut):
        mut_index.append(random.randint(0,23))
        mut_value.append(random.randint(0,30))
        cr_num=mut_index[i]//4
        gen_num=mut_index[i]%4
        new_pop[cr_num][-(gen_num-1)]=mut_value[i]

    print("After iteration: ",it," Population is")
    print(new_pop)
    print(obj)
    pop1=new_pop
