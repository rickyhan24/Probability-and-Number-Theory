#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages

import sympy
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import scipy.stats as stats
import scipy


# In[2]:


#Define a function that gives largest power of two that is a factor of a given number

def largestPowerOfTwoThatIsAFactorOf(num):
    if num % 2 != 0: return 1
    factor = 0
    while num % 2 == 0:
        num /= 2
        factor += 1
    return factor


# In[3]:


#Examine the powers of 2 for the sequence of positive integers.
m=1000

M=[]
for i in range(1, m+1):
    if i%2==0:
        
        k=largestPowerOfTwoThatIsAFactorOf(i)
        
        M.append(k)
    else:
      M.append(0)
print(set(M))
#Plot histogram

fig, ax = plt.subplots()
ax.hist(M, bins=len(set(M)), rwidth=.9)
ax.set_title('Highest Powers of 2 for first 1000 Positive Integers') # Title
ax.set_xlabel('x=highest power of 2')  # X axis label
ax.set_ylabel('count')  # Y axis label
plt.xticks(M)
plt.show()

#Get the bin sizes
n, bins, patches = plt.hist(M, bins=len(set(M)))
print('Bin sizes:', n)


# In[4]:


#Find the chi-squared value
Sum=sum(M)
print('Sum of the xi is:', Sum)
k=len(set(M))-1
def E(x):
  return m*(scipy.special.comb(k,x))*((Sum/(k*m))**x)*((1-Sum/(k*m))**(k-x))

Ex=np.array([E(i) for i in range(k+1)])
Ox=np.array(n)
Chi_squared = np.sum(((Ox-Ex)**2)/Ex)
print('Chi_squared:',Chi_squared)


# In[5]:


#calculate sample mean and sample variance of X
print('sample variance:',sum((np.array(M)-(Sum/m))**2)/(m-1))
print('sample mean:',Sum/m)


# In[8]:


import random
m=10000
random.seed(4)
# Generate unique random numbers within a range
num_list = random.sample(range(1, 100000), m)
print(num_list)


# In[9]:


#Examine the powers of 2 for the sequence of random numbers.


M=[]
for i in num_list:
    if i%2==0:
        
        k=largestPowerOfTwoThatIsAFactorOf(i)
        
        M.append(k)
    else:
      M.append(0)
print(set(M))
#Plot histogram

fig, ax = plt.subplots()
ax.hist(M, bins=len(set(M)), rwidth=.9)
ax.set_title('Highest Powers of 2 for 10,000 Random Positive Integers') # Title
ax.set_xlabel('x=highest power of 2')  # X axis label
ax.set_ylabel('count')  # Y axis label
plt.xticks(M)
plt.show()

#Get the bin sizes
n, bins, patches = plt.hist(M, bins=len(set(M)))
print('Bin sizes:', n)


# In[10]:


#Find the chi-squared value
Sum=sum(M)
print('Sum of the xi is:', Sum)
k=len(set(M))-1
def E(x):
  return m*(scipy.special.comb(k,x))*((Sum/(k*m))**x)*((1-Sum/(k*m))**(k-x))

Ex=np.array([E(i) for i in range(k+1)])
Ox=np.array(n)
Chi_squared = np.sum(((Ox-Ex)**2)/Ex)
print('Chi_squared:',Chi_squared)


# In[11]:


#calculate sample mean and sample variance of X
print('sample variance:',sum((np.array(M)-(Sum/m))**2)/(m-1))
print('sample mean:', Sum/m)


# In[ ]:




