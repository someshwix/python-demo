import multiprocessing as mp

def insert_record(record, records):
    print("I am child process for inserting a record")
    records.append(record)
    print("New record is added!\n")

def print_record(records):
    print("I am child process for printing records")
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))       

if __name__ == '__main__':
    print("I am the parent process:")
    
    with mp.Manager() as manager:
        print("I am the server process")
        
        # Create a shared list using Manager
        records = manager.list([('Murthy', 10), ('Sriram', 9), ('Kiran', 9)])
        new_record = ('Malika', 8)  # Define the new record as a tuple
        
        # Create child processes
        p1 = mp.Process(target=insert_record, args=(new_record, records))
        p2 = mp.Process(target=print_record, args=(records,))
        
        # Start and join processes
        p1.start()
        p1.join()  # Ensure record is added before printing
        
        p2.start()
        p2.join()