#oops module 
class Employee(object):
    #constructoer
    def __init__(self,empno,ename,salary):
        self.eno=empno
        self.name=ename
        self.pay=salary
        
    def showDetails(self):
        print('Epmno',self.eno)
        print('Ename',self.name)
        print('Salry',self.pay)    

if __name__=='__main__':
    e1=Employee(101,'somesh',5000)
    e1.showDetails()      