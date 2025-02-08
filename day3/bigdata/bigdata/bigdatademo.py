import pandas as pd
'''
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(data_url, sep=';')
print(data)

my_new_series = data['chlorides']
print(my_new_series)

#data.dropna()
#data.fillna(0)
print(data.fillna(data.mean()))
print(data.sort_values('density'))
'''

'''
A mebibyte (MiB) is a multiple of the unit byte. It represents a unit of digital information
 storage used to denote the size of data. It is equivalent to  1,048,576, bytes.

 462Mib = 484442112 bytes  = 473088 kb = 484MB

'''
import pandas as pd
import psutil
 
import multiprocessing as mp

# Check the number of cores and memory usage
num_cores = mp.cpu_count()
print("This kernel has ",num_cores ,"Cores" )
print("Memory usage:",psutil.virtual_memory())


# Loading the training dataset by chunking dataframe
memory_timestep_1 = psutil.virtual_memory()
 #taxi data :  
 # https://www.kaggle.com/datasets/edwinytleung/nyc-yellow-taxi-2015-sample-data?resource=download
data_iterator = pd.read_csv("data.csv", chunksize=100000)
fare_amount_sum_chunk = 0
for data_chunk in data_iterator:
  fare_amount_sum_chunk += data_chunk['fare_amount'].sum()
 
memory_timestep_2 = psutil.virtual_memory()
 
memory_used_pd = (memory_timestep_2[3] - memory_timestep_1[3])/(1024*1024)
print("Memory acquired with chunking the dataframe: %.4f MB"%memory_used_pd)
 
 
# Loading the training dataset using pandas
memory_timestep_3 = psutil.virtual_memory()
 
training_data_pd = pd.read_csv("data.csv")
fare_amount_sum_pd = training_data_pd['fare_amount'].sum()
 
memory_timestep_4 = psutil.virtual_memory()
 
memory_used_pd = (memory_timestep_4[3] - memory_timestep_3[3])/(1024*1024)
print("Memory acquired without chunking the dataframe: %.4f MB"%memory_used_pd)


