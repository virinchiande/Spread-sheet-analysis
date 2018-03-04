
# coding: utf-8

# <h1>Simple Spreadsheet Analysis</h1>

# <h3>Ravindra Rashmi Dasappa</h3>

# <h5>Importing the Data</h5>

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/rahmi/Desktop/HireArt.csv")
data.head(5)


# <h5>Exploring the Data</h5>

# In[122]:

data.info()


# In[2]:

data['year'], data['month'], data['day'] = zip(*data['Date of Contact'].map(lambda x: x.split('-')))


# In[3]:

data.head(5)


# In[99]:

pd.DataFrame(data['Account manager'].unique(),columns = ['Account Manager Names'])


# This shows the no of clients who were contacted atleast once by the account managers on different dates

# In[111]:

grouped = data.groupby('Account manager')
no_of_clients_manager = grouped['Client Name'].count() 
pd.DataFrame(no_of_clients_manager)


# The below result shows the number of clients who contacted in a perticular year.

# In[112]:

grouped = data.groupby('year')
no_of_clients_contacted_year= grouped['Client Name'].count() 
pd.DataFrame(no_of_clients_contacted_year)


# The result below shows that each year same number of unique clients are contacted

# In[113]:

grouped = data.groupby('year')
no_of_clients_contacted_year= grouped['Client Name'].nunique() 
pd.DataFrame(no_of_clients_contacted_year)


# In[101]:

pd.DataFrame(data['Client Name'].unique(),columns = ['Client Names'])


# The result below shows that each month number of clients contacted more than once across all years. It shows that October month has the highest number of clients contacted more than once across all years.

# In[118]:

grouped = data.groupby('month')
no_of_clients = grouped['Client Name'].count().sort_values(ascending = False)
pd.DataFrame(no_of_clients)


# The result below shows that each month number of unique clients contacted across all years. It shows that October month has the highest number of unique clients contacted across all years.

# In[133]:

def time_contact_clients():
    grouped = data.groupby('month')
    no_of_clients = grouped['Client Name'].nunique() 
    my_dict = {}
    j =0
    for i in grouped:
        my_dict[i[0]]=no_of_clients[j]
        j = j+1
    maximum = max(my_dict, key=my_dict.get)
    print("The month to contact the most clients: \n",maximum,"month as max number of unique clients contacted across all years with",my_dict[maximum],"unique clients")
    #print(my_dict)


# In[134]:

time_contact_clients()


# In[11]:

def perc_contact_clients():
    no_unique_clients_total = data['Client Name'].nunique()
    grouped = data.groupby('month')
    no_of_clients = grouped['Client Name'].nunique()
    perc = (no_of_clients/no_unique_clients_total) * 100
    my_dict = {}
    j =0
    for i in grouped:
        my_dict[i[0]]=perc[j]
        j = j+1
    maximum = max(my_dict, key=my_dict.get)  
    print("The month to contact the most clients: \n",maximum)
    print(perc)


# In[12]:

perc_contact_clients()


# The results below shows the year and month in which most of unique clients were contacted

# In[161]:

def perc_contact_clients_year():
    no_unique_clients_total = data['Client Name'].nunique()
    grouped = data.groupby(['year', 'month'])
    no_of_clients = grouped['Client Name'].nunique()
    perc = (no_of_clients/no_unique_clients_total) * 100
    my_dict = {}
    j =0
    for i in grouped:
        my_dict[i[0]]=perc[j]
        j = j+1
    maximum = max(my_dict, key=my_dict.get)  
    print("The year and month in which most unique clients were contacted across all years: \n",maximum)
    
   


# In[162]:

perc_contact_clients_year()


# In[159]:

def perc_contact_clients_month_year():
    
    years = list(data.year.unique())
    for y in years:
        data_year = data[data['year'] == y]
        grouped = data_year.groupby(['month'])
        no_of_clients = grouped['Client Name'].nunique()
        no_unique_clients_total = data_year['Client Name'].nunique()
        perc = (no_of_clients/no_unique_clients_total) * 100
        my_dict = {}
        j =0
        for i in grouped:
            my_dict[i[0]]=perc[j]
            j = j+1
        maximum = max(my_dict, key=my_dict.get)  
        print("In the year",y,"month in which max no of unique clients conatcted is:",maximum,"with",round(my_dict[maximum],4),"percentage ")
        plt.bar(range(len(my_dict)), list(my_dict.values()), align='center')
        plt.xticks(range(len(my_dict)), list(my_dict.keys()))
        plt.show()


# In[160]:

perc_contact_clients_month_year()


# In[ ]:



