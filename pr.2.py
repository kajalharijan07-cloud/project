print("welcome to the pettern generator and number analyzer!")
print("select an option:")
print("1. generate a pettern")
print("2. analyze a range of numbers")
print("3. exit")
a=int(input("enter your choice:"))

if a==1:
    n=int(input("enter the number of rows for the pattern:"))
    print("pattern:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif a==2:
    a=int(input("enter the start of the range:"))
    b=int(input("enter the end of the range:"))
    for i in range(a,b+1):
        if i%2==0:
            print(i,"number is even")
        else:
            print(i,"number is odd")
    print("sum of all numbers from",a,"to",b,"is:",sum(range(a,b+1)))
elif a==3:
    print("exiting the program. Goodbye!")
else:
    print("invalid choice")
    
