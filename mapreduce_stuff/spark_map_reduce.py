
# coding: utf-8

# In[3]:

import findspark
findspark.init()
from pyspark import SparkContext 

sc = SparkContext.getOrCreate() 
raw_data = sc.textFile("daily_show_guests.csv")
raw_data.take(5)


# In[5]:

ds = raw_data.map(lambda line: line.split(","))
ds.take(5)


# In[7]:

tally = ds.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)
print(tally)


# In[8]:

tally.take(tally.count())


# In[10]:

ds.filter(lambda line: line[1] != '').map(lambda line: (line[1].lower(), 1)).reduceByKey(lambda x,y: x+y).take(5)


# In[ ]:



