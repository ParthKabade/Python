def main():
    Ans=0
    try:
      print("Enter 1st Number")
      No1=int(input())

      print("Enter 2nd Number")
      No2=int(input())

      Ans=No1/No2
      print("Division is succeful")

    except Exception as eobj:    
       print("Exception occured :",eobj)

    
       
    print("Result is :",Ans)


if __name__=="__main__":
    main()