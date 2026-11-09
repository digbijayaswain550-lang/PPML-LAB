n=float(input("Enter the percentage:"))
if(n>=90 and n<=100):
    print("O grade",n)
elif(n<=90 and n>=80):
    print("E grade",n)
elif(n<=80 and n>=70):
    print("A grade",n)
elif(n<=70 and n>=60):
    print("B grade",n)
elif(n<=60 and n>=50):
    print("C grade",n)
elif(n<=50 and n>=40):
    print("D grade",n)
else:
    print("FAIL")
