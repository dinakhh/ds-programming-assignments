#!/usr/bin/env python
# coding: utf-8

# In[1]:


personWeight=float(input("enter your weight in kilograms please: "))
personHeight=float(input("enter your height in CM please: "))
personHeightInMeters=personHeight/100.0
BMI=personWeight/personHeightInMeters**2
print("BMI=" ,BMI)


# In[3]:


personWeight=float(input("enter your weight in pounds please: "))
personHeight=float(input("enter your height in inches please: "))
personWeightinKilograms=personWeight/2.2046
personHeightInMeters=personHeight/39.37
BMI=personWeightinKilograms/personHeightInMeters**2
print("BMI=" ,BMI)


# In[ ]:




