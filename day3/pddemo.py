import pandas as pd

# Corrected dictionary key typo and method usage
data = {'apples': [3, 2, 0, 1], 'orange': [0, 3, 7, 2]}
purchases = pd.DataFrame(data, index=['somesh', 'rahul', 'jeba', 'shukla'])

print(purchases.tail(2))
print(purchases.loc['somesh'])
print(purchases.shape)