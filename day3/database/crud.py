import sqlite3  # Fixed spelling error
from employee import Employee

def connectDB():
    global conn, cursor  # Define both conn and cursor globally
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()  # Fixed spelling error
    print("Connected to database")

def createTable():
    try:
        cmd = "CREATE TABLE IF NOT EXISTS emps(fname TEXT, lname TEXT, pay INTEGER)"
        cursor.execute(cmd)  # Fixed variable name
        conn.commit()
        print("emps table created ")
    except Exception as ex:
        print("Cannot create table:", ex)

def insertEmp(emp):
    try:
        cmd = "INSERT INTO emps (fname, lname, pay) VALUES (?, ?, ?)"
        values = (emp.fname, emp.lname, emp.pay)
        cursor.execute(cmd, values)
        conn.commit()
        print("One employee added to database table")
    except Exception as ex:
        print("Error in inserting:", ex)

def readEmps():
    cursor.execute("SELECT*FROM emps")
    return cursor.fetchall()

def deleteEmp(emp):
    cursor.execute("DELETE FROM emps WHERE lname = :last", {'last': emp.lname})


# Test code
print("Working with sqlite3 database")
connectDB()  # Fixed spelling error
# createTable()
#emp1 = Employee('Murthy', 'saikiran', 50000)
#emp2 = Employee('kiran', 'kumar', 40000)
#insertEmp(emp1)
#insertEmp(emp2)

data=readEmps()
print(data)
print("after deleteing")
emp1 = Employee('Murthy', 'saikiran', 50000)
deleteEmp(emp1)

data=readEmps()
print(data)

cursor.close()
conn.close()  # Fixed memory leak