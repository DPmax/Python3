# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:41:52 2017

@author: LONGCHENG
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def ExperimentalBT(N):
    n = 1000
    successfulTrials = []
    #N times of experiments
    for k in range(N):
        currentTrial = 0
        #Roll 1000 times three fair dice
        for j in range(n):
            count = 0
            for l in range(3):
                #Whenever rolls "SIX" count increase
                if np.random.randint(1, 7) == 6:
                    count = count + 1;
            #Whenever "SIX" appears 3 times count as success for experiment
            if count == 3:
                currentTrial = currentTrial + 1
        successfulTrials.append(currentTrial)
        
    #Plot probability
    b = range(-1,17)
    h1, bin_edges = np.histogram(successfulTrials, bins = b)
    b1 = bin_edges[0:17]
    plt.stem(b1, h1/N)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in N trials")
    
def BinomialD(N):
    combi = []
    #Roll three dice the P = 1/6^3
    probability = 1/216
    #After 14 there is almost always 0
    for x in range(17):
        # combination 
        c = sp.misc.comb(N,x, 1, 1)
        # success
        p = np.power(probability, x)
        # failure
        q = np.power(1-probability, N-x)
        
        #Binomial formula p(X=x)=NCx * p^x * q^(n-x)
        for k in range((int)(c * p * q * N)):
            combi.append(x)
        
    b = range(-1,17)
    h1, bin_edges = np.histogram(combi, b)
    b1 = bin_edges[0:17]
    plt.stem(b1, h1/N)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in N trials")

def PoissonD(N):
    #Roll three dice the P = 1/6^3
    probability = 1/216
    #The parameter λ = np
    lda = probability * N
    eulersnumber = 2.7182818284
    poisson = []
    #After 14 there is almost always 0
    for i in range(17):
        # a = λ^x
        a = np.power(lda,i) 
        # b = e ^ (-λ)
        b = np.power(eulersnumber,-lda)
        # c = x!
        c = np.math.factorial(i)
        
        # p(X=x)= [λ^x * e^(-λ)] / x!
        x = (int)(a * b * N/ c);
        
        for k in range(x):
            poisson.append(i)
        
    b = range(-1,17)
    h1, bin_edges = np.histogram(poisson, bins = b)
    b1 = bin_edges[0:17]
    
    plt.stem(b1, h1/N)
    plt.title("Probability Mass Function")
    plt.ylabel("Probability of success")
    plt.xlabel("Number of successes in N trials")
    

ExperimentalBT(10000)
BinomialD(1000)
PoissonD(1000)
