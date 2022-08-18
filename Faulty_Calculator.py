print("Enter two two nubers to calculate ")
a =int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("Choose a function to do the operation : '+'-'%'*'/' : ")
c=input()



if a == 44 and b == 3 and c == '*':print("Your answer is  : 555")
elif a == 56 and b == 9 and c == '+':print("your answer is : 77")
elif a == 56 and b == 6 and c == '/':print("your answer is : 71")
elif c=='+':
    d=a*b
    print(d)
elif c == '-':
    e = a * b
    print(e)
elif c=='*':
    f=a*b
    print(f)
elif c=='/':
    g=a*b
    print(g)
else:
    print("Out of range")