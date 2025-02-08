import pandas as pd
import psutil
 
# Loading the training dataset by chunking dataframe
memory_timestep_1 = psutil.virtual_memory()
 #drop columns
columns = ['fare_amount', 'trip_distance']
data_1 = pd.read_csv("data.csv", usecols=columns)
 
memory_timestep_2 = psutil.virtual_memory()
 
memory_used_pd = (memory_timestep_2[3] - memory_timestep_1[3])/(1024*1024)
print("Memory acquired by sampling columns: %.4f MB"%memory_used_pd)
 
 
# Loading the training dataset using pandas
memory_timestep_3 = psutil.virtual_memory()
 
data_2 = pd.read_csv("data.csv")
 
memory_timestep_4 = psutil.virtual_memory()
 
memory_used_pd = (memory_timestep_4[3] - memory_timestep_3[3])/(1024*1024)
print("Memory acquired without sampling columns: %.4f MB"%memory_used_pd)
