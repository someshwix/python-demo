def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                print(f"called {i+1} time(s)")
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator
#------------------------------------------

numtimes=3
@repeat(n=numtimes)
def task(name):
    print(f"Excuted task with {name}")

task('upload')