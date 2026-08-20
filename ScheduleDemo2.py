import schedule 
import time
import datetime

def Display():
    print(f"Jay Ganesh... {datetime.datetime.now()}")

def main():
    print(f"Automation Script Started ")

    schedule.every(1).minute.do(Display)
    #code मध्ये मुख्य Issue म्हणजे तू job schedule केली आहेस, पण scheduler चालूच केलेला नाही.
"""
Internally काय होतं?

Step 1
schedule.every(1).minute.do(Display)

Internally schedule library एक Job Object तयार करते.

Job
------------------------
Function : Display
Interval : 1
Unit     : minute
Next Run : Current Time + 1 minute
------------------------

हा job एका list मध्ये store केला जातो.
Jobs List

Job1
 ├── Function -> Display
 ├── Every -> 1 minute
 └── Next Run -> 10:30:00
"""

if __name__=="__main__":
    main()

