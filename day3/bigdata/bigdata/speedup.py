import pandas as pd
from sys import getsizeof
 
data = pd.read_csv("data.csv")
 
size = getsizeof(data)/(1024*1024)
print("Initial Size: %.4f MB"%size)
 
# chaning VendorID to boolean
data.VendorID = data.VendorID.apply(lambda x: x==2)
 
# chaning pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude to float32
location_columns = ['pickup_latitude','pickup_longitude',
                    'dropoff_latitude','dropoff_longitude']
data[location_columns] = data[location_columns].astype('float32')
 
# chaning payment_type to categorical
data.payment_type = data.payment_type.astype('category')
 
size = getsizeof(data)/(1024*1024)
print("Size after reduction: %.4f MB"%size)