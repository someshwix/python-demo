def square_numbers(nun):
    for i in nums:
        yield(i*i)
        
my_nums=square_numbers([1,2,3,4,5])
print(type(my_nums))
print(next(my_nums))
print(next(my_nums))        
