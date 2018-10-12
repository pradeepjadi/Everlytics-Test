
# coding: utf-8

# In[2]:


import pandas as pd 
import os
os.getcwd()

data = pd.read_csv("E:\\Data Science\\notes and data\\Datasets-20180426T120531Z-001\\Datasets\\MFGEmployees4.csv") 
len(data)
data.head() 
data.columns
#fix the spaces in the columns movies.columns = [...]
data.head()
 


# In[3]:


print(data.columns)


# In[4]:


data.hist()


# In[6]:


data.info() #ntc year, is this a numeric or cat,

data.describe() 


# In[7]:


data.describe() 
#ntc year, ds it make sense, v dnt want treat yr as num but cat


# In[8]:


#Convert it to catgry var
data.Gender = data.Gender.astype('category')
data.info() #ntc it is now category #factors in R


# In[9]:


data.describe() 


# In[11]:



from matplotlib import pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[12]:


#JoinPlot

j = sns.jointplot(data=data,x='Age',y='EmployeeNumber')
j = sns.jointplot(data=data,x='Age',y='EmployeeNumber',kind='hex')


# In[17]:


# Gender barplot

j = sns.jointplot(data=data,x='Gender',y='EmployeeNumber')
j = sns.jointplot(data=data,x='Gender',y='EmployeeNumber',kind='hex')





# In[14]:


# City barplot

j = sns.jointplot(data=data,x='City',y='EmployeeNumber')
j = sns.jointplot(data=data,x='City',y='EmployeeNumber',kind='hex')


# In[16]:



# JobTitle barplot

j = sns.jointplot(data=data,x='JobTitle',y='EmployeeNumber')
j = sns.jointplot(data=data,x='JobTitle',y='EmployeeNumber',kind='hex')
j.plot(y,x)


# In[20]:


plt.scatter(data.Gender,data.EmployeeNumber)


# In[28]:


plt.scatter(data.EmployeeNumber/2,data.Gender)
plt.xlabel('count')
plt.ylabel('Gender')
plt.title("gender plot")


# In[30]:


plt.scatter(data.EmployeeNumber/2,data.JobTitle)
plt.xlabel('count')
plt.ylabel('JobTitle')
plt.title("Job Title plot")


# In[32]:


plt.scatter(data.EmployeeNumber/2,data.StoreLocation)
plt.xlabel('count')
plt.ylabel('StoreLocation')
plt.title(" StoreLocation plot")


# In[39]:


EmployeeNumbers = pd.factorize(data.EmployeeNumber)
EmployeeNumbers
Genders=data.Gender

plt.scatter(data.EmployeeNumber,data.Gender)
plt.xlabel('count')
plt.ylabel('Gender')
plt.title("gender plot")


# In[43]:


EmployeeNumber1= pd.factorize(data.EmployeeNumber)
StoreLocation1= pd.factorize(data.StoreLocation)

plt.scatter(data.EmployeeNumber,data.StoreLocation)
plt.xlabel('count')
plt.ylabel('Gender')
plt.title("gender plot")


# In[45]:



plt.scatter(data.EmployeeNumber,data.Division)
plt.xlabel('count')
plt.ylabel('Division')
plt.title("Division plot")


# In[46]:




plt.scatter(data.EmployeeNumber,data.BusinessUnit)
plt.xlabel('count')
plt.ylabel('BusinessUnit')
plt.title("BusinessUnit plot")

