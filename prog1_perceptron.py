import numpy as np    
class Perceptron(object):
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta # Learning rate (between 0.0 and 1.0)
        self.n_iter = n_iter # Passes over the training dataset.
    def fit(self, X, y):
       
        self.w_ = np.zeros(1 + X.shape[1])
        
        for _ in range(self.n_iter):
            
            for xi, target in zip(X, y):
                error=target-self.predict(xi)
                if error!=0:
                    update = self.eta * (self.predict(xi))
                    self.w_[1:] += update * xi
                    self.w_[0] += update
                
            
        return self
    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]
    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

import pandas as pd
import matplotlib.pyplot as plt
# inpur of 8 x 3
X=np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
print(' Inputs : \n',X)
# target
y=np.array([-1,-1,-1,-1,1,1,1,1])
## call perceptron
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
## predict o/ps
print('outpusts ', ppn.predict(X))
print(' output for [1,1,1] is ',ppn.predict([1,1,1]))
print(' output for [0,0,0] is ',ppn.predict([0,0,0])) # predicting o/p for given inputs
