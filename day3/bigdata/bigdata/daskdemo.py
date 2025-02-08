import pandas as pd
import dask.dataframe as ddf
import psutil

'''
Dask is a parallel computing library, which scales NumPy, pandas, 
and scikit module for fast computation and low memory. 

It uses the fact that a single machine has more than one core,
 and dask utilizes this
 fact for parallel computation.

pip install dask

We can use dask data frames which is similar to pandas data frames. 

A dask data frame consists of multiple smaller pandas data frames under
 the hood. A method call on a single Dask DataFrame is making many pandas method 
 calls, and Dask knows how to coordinate everything to get the result.
'''
#Loading the training dataset using dask
memory_timestep_3 = psutil.virtual_memory()
 
training_data_ddf = ddf.read_csv("data.csv")
 
memory_timestep_4 = psutil.virtual_memory()
 
memory_used_ddf = (memory_timestep_4[3] - memory_timestep_3[3])/(1024*1024)
print("Memory acquired using dask: %.4f MB"%memory_used_ddf)
 
 
# Loading the training dataset using pandas
memory_timestep_1 = psutil.virtual_memory()
 
training_data_pd = pd.read_csv("data.csv")
 
memory_timestep_2 = psutil.virtual_memory()
 
memory_used_pd = (memory_timestep_2[3] - memory_timestep_1[3])/(1024*1024)
print("Memory acquired using pandas: %.4f MB"%memory_used_pd)