def check(x):
    '''check fn takes values in string....'''
 #   if x.startswith('M'):
  #      return True
 #   else 

# single line function are the lambda function 
#add5=lambda x:x+5

#print(type(add5))
#print(add5(100))

#sm=lambda x:True if x.startswith('M') else False
#print(sm("murthy"))
#alist=["learn","python","steps"]
#output=map(lambda x:x.upper(),alist)
#print(type(output))

#filter
#scores = [66,90,68,76,60,88,89,81]
#def is_A_student(score):
#    return score > 75

#checker=lambda x:x>75
#over_75 = list(filter(checker,scores))
#print(over_75)

#sort
#list1=[("eggs",5.25),("honey",9.5),("carrots",1.4)]
#list1.sort(key =lambda x:x[1],reverse=0)
#true=1 False=0
#print(list1)

import numpy as np
x = np.array([1,2,3,4,5,6])
#print array of square of each elemnets in x
squarer = lambda t: t**2
squares = np.array([squarer(xi)for xi in x])
print(squares)