import schedule,time

def upload():
    print("upload started.......")# do actual work 
schedule.every(1).minute.do(upload)
schedule.every().monday.do(upload)

while True:
    schedule.run_pending()
    time.sleep(10)
    print('*')

