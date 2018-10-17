from matplotlib import pyplot as plt
import numpy as np
plt.figure(1) # create new figure
plt.subplot(211)#create subplot

plt.plot([1,2,3,4]) # X-axis creates automatically
plt.subplot(212)
plt.plot([1,2,3,4],[1,4,9,6]) #plot between x,y
#plt.figure(2)

plt.plot([1,2,3,4],[1,4,9,6],'yo') # plot for red color,o
plt.xlabel("x")
plt.ylabel("y",fontsize=10,color='red')
plt.title("Graph2")

plt.text(2,2,"Hi")

plt.axis([0,6,0,20])

plt.grid(True)
plt.show()
#plt.figure(3)
plt.subplot(221)
t=np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
####
plt.scatter(gdp_cap, life_exp,s=size,c=color,alpha=0.8) #opacity
# Put the x-axis on a logarithmic scale


plt.xscale('log')

# histogram
plt.hist(x,bins=10)  # used for distrubution
plt.clf() # clear the plot
####Customization
tick_val = [1000,10000,100000]

tick_lab = ['1k','10k','100k']


# Adapt the ticks on the x-axis

plt.xticks(tick_val,tick_lab)
plt.text(5700, 80, 'China')
####
