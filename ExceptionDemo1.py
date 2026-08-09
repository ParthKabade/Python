


def main():
    print("Enter 1st Number")
    No1=int(input())

    print("Enter 2nd Number")
    No2=int(input())

    Ans=No1/No2

    print("Result is :",Ans)


if __name__=="__main__":
    main()

"""
parthkabade@Parths-MacBook-Air py_cw % python3 exceptiondemo1.py
Enter 1st Number
12
Enter 2nd Number
0
Traceback (most recent call last):
  File "/Users/parthkabade/Desktop/Python/Py_Cw/exceptiondemo1.py", line 17, in <module>
    main()
    ~~~~^^
  File "/Users/parthkabade/Desktop/Python/Py_Cw/exceptiondemo1.py", line 11, in main
    Ans=No1/No2
        ~~~^~~~
ZeroDivisionError: division by zero
"""