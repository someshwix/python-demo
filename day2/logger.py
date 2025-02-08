def logger(func):
    def wrapper():
        print(f"someone called {func.__name__}")
        func()
        print(f"{func.__name__} is executed successfully")
    return wrapper
#----------------------------        

@logger
def processData():
    print("conneting to db ")
    print("data proccess")

processData()
