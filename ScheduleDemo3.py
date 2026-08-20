import schedule 
import time
import datetime

def Display():
    print(f"Jay Ganesh... {datetime.datetime.now()}")

def main():
    print(f"Automation Script Started ")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(.5)
    print(f"End of automation script")

if __name__=="__main__":
    main()