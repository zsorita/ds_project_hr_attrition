#!/usr/bin/env python
# coding: utf-8

# # HR Attrition

# SETUP

# In[1]:


# !pip install kmodes


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import OneHotEncoder
sns.set_theme(style='white', palette='deep')

import warnings
warnings.filterwarnings("ignore")

from kmodes.kmodes import KModes


# In[3]:


attrition_data = pd.read_csv("IBM_HR-Attrition.csv")
attrition_data.head(2)


# # Drop unnecessary columns

# In[4]:


attrition_data.drop(columns=["EmployeeCount", "EmployeeNumber", "StandardHours", "StockOptionLevel"], inplace=True)


# In[5]:


attrition_data.info()


# In[6]:


attrition_data.describe().T


# In[7]:


attrition_data.isnull().any()


# In[8]:


attrition_data.isna().any()


# In[9]:


attrition_data.columns


# In[10]:


# numeric and categorical columns
num_col = attrition_data.describe().columns.tolist()
cat_col = attrition_data.describe(include="object").columns.tolist()

# num_col
# cat_col


# In[11]:


corr = attrition_data[num_col].corr()
corr


# In[12]:


cmap = sns.diverging_palette(180, 10, as_cmap=True)
sns.heatmap(corr, vmax=.3, center=0, cmap=cmap, square=True)
plt.show()


# In[13]:


Attrition_Yes = attrition_data[attrition_data["Attrition"] == "Yes"]
Attrition_No = attrition_data[attrition_data["Attrition"] == "No"]
Attrition_Mean = pd.concat((Attrition_Yes.mean(numeric_only=True), Attrition_No.mean(numeric_only=True)), axis=1)
Attrition_Mean.columns = ["Yes","No"]
Attrition_Mean.round(2).style.background_gradient(cmap="Pastel1",axis=1)


# In[14]:


Attrition_Yes["Attrition"].value_counts() 
# = 237


# In[15]:


Attrition_No["Attrition"].value_counts()
# = 1233


# # EXPLORATORY DATA ANALYSIS

# # Attrition Count

# In[16]:


chart_1=sns.countplot(x="Attrition", data=attrition_data).set(xlabel=None, ylabel=None)
plt.show()


# # Correlation

# Determine numeric and categorical values.

# In[17]:


# numeric and categorical columns
num_col = attrition_data.describe().columns.tolist()
cat_col = attrition_data.describe(include="object").columns.tolist()

# num_col
# cat_col


# In[18]:


corr = attrition_data[num_col].corr()
corr


# In[19]:


cmap = sns.diverging_palette(180, 10, as_cmap=True)
sns.heatmap(corr, vmax=.3, center=0, cmap=cmap, square=True)
plt.show()


# # Age

# In[20]:


sns.histplot(data=attrition_data, x="Age", hue="Attrition", kde=True).set(xlabel=None, ylabel=None)
plt.show()


# # Gender

# In[21]:


sns.countplot(data=attrition_data, x="Gender", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Marital Status

# In[22]:


sns.histplot(data=attrition_data, x="MaritalStatus", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Department

# In[23]:


sns.countplot(data=attrition_data, x="Department", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# In[24]:


dept_data = attrition_data[attrition_data['Department'] == 'Research & Development']

sns.countplot(data=dept_data, y='JobRole', hue='Attrition')
plt.show()


# # Satisfaction

# In[25]:


sns.countplot(data=attrition_data, x="EnvironmentSatisfaction", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Job Satisfaction

# In[26]:


sns.countplot(data=attrition_data, x="JobSatisfaction", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Travel

# In[27]:


sns.countplot(data=attrition_data, x="BusinessTravel", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Overtime

# In[28]:


sns.histplot(data=attrition_data, x="OverTime", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Total Working Years

# In[29]:


sns.histplot(data=attrition_data, x="TotalWorkingYears", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Years at Company

# In[30]:


sns.histplot(data=attrition_data, x="YearsAtCompany", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Years In Current Role

# In[31]:


sns.histplot(data=attrition_data, x="YearsInCurrentRole", hue="Attrition").set(xlabel=None, ylabel=None)
plt.show()


# # Monthly Income

# In[32]:


sns.displot(data=attrition_data, x="MonthlyIncome", hue="Attrition", kind="kde")
plt.show()


# # Distance From Home

# In[33]:


sns.displot(data=attrition_data, x="DistanceFromHome", hue="Attrition", kind="kde")
plt.show()


# # Clustering

# In[34]:


def run_kmodes(n_clusters=None, filtered_data_cluster=None):
  # Initialize clustering
  kmodes = KModes(
      init="random",
      n_clusters=n_clusters,
      random_state=42
      )
  
  # Apply clustering to the data
  kmodes.fit(attrition_data)

  # Print intertia
  print(f"Cost for n_clusters = {n_clusters}: {kmodes.cost_}")

  return kmodes.cost_, kmodes.labels_


# In[35]:


cost_values = []


# In[36]:


for k in range(1, 21):
  # Run our function
  cost, labels = run_kmodes(
    n_clusters=k,
    filtered_data_cluster=attrition_data
  )

  # Save cost to our container
  cost_values.append(cost)


# In[37]:


# Set figure size
plt.figure(figsize=(6,3)  , dpi=200)

# Plot inertia vs number of clusters
plt.plot(range(1, 21), cost_values)

# Format plot
plt.xticks(range(1, 21))
plt.xlabel("Number of Clusters")
plt.ylabel("Cost")

# Show plot
plt.show()


# In[38]:


# Run our K-Modes function for n_clusters
cost, labels = run_kmodes(
  n_clusters=9,
  filtered_data_cluster=attrition_data
)


# In[39]:


attrition_data['labels']= labels
attrition_data


# In[40]:


attrition_data['labels'].value_counts().sort_index()


# In[41]:


attrition_data.groupby('labels').agg(pd.Series.mode)


# In[42]:


# clustered_data_1 = attrition_data.groupby('labels').agg(pd.Series.mode)
# clustered_data_1.to_csv('clustered_data_1', index=False)
