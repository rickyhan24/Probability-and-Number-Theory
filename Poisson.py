#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Import packages

import sympy
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import scipy.stats as stats
import scipy


# In[6]:


#Define a function that gives largest power of two that is a factor of a given number

def largestPowerOfTwoThatIsAFactorOf(num):
    if num % 2 != 0: return 1
    factor = 0
    while num % 2 == 0:
        num /= 2
        factor += 1
    return factor


# In[7]:


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
ax.set_title('Histogram plot') # Title
ax.set_xlabel('X axis label')  # X axis label
ax.set_ylabel('Y axis label')  # Y axis label
plt.xticks(M)
plt.show()

#Get the bin sizes
n, bins, patches = plt.hist(M, bins=len(set(M)))
print('Bin sizes:', n)


# In[8]:


math.factorial(3)


# In[9]:


#Find the chi-squared value
Sum=sum(M)
print('Sum of the xi is:', Sum)
k=len(set(M))-1
def E(x):
  return m*(math.exp(-Sum/m))*((Sum/m)**x)/(math.factorial(x))

Ex=np.array([E(i) for i in range(k+1)])
Ox=np.array(n)
Chi_squared = np.sum(((Ox-Ex)**2)/Ex)
print('Chi_squared:',Chi_squared)


# In[10]:


#calculate sample mean and sample variance of X
print('sample variance:',sum((np.array(M)-(Sum/m))**2)/(m-1))
print('sample mean:',Sum/m)


# In[11]:


import random
m=10000
random.seed(4)
# Generate unique random numbers within a range
num_list = random.sample(range(1, 100000), m)
print(num_list)


# In[12]:


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
ax.set_title('Histogram plot') # Title
ax.set_xlabel('X axis label')  # X axis label
ax.set_ylabel('Y axis label')  # Y axis label
plt.xticks(M)
plt.show()

#Get the bin sizes
n, bins, patches = plt.hist(M, bins=len(set(M)))
print('Bin sizes:', n)


# In[13]:


#Find the chi-squared value
Sum=sum(M)
print('Sum of the xi is:', Sum)
k=len(set(M))-1
def E(x):
  return m*(math.exp(-Sum/m))*((Sum/m)**x)/(math.factorial(x))

Ex=np.array([E(i) for i in range(k+1)])
Ox=np.array(n)
Chi_squared = np.sum(((Ox-Ex)**2)/Ex)
print('Chi_squared:',Chi_squared)


# In[14]:


#calculate sample mean and sample variance of X
print('sample variance:',sum((np.array(M)-(Sum/m))**2)/(m-1))
print('sample mean:', Sum/m)


# In[ ]:




