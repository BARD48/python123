a,b=int(input())
def main():
    x=int(input("What is the number"))
    y=int(input("what is the second number"))
    print(f"{x} squere is {square(x)}")
    print(f"When the {x} is subtracted from the {y} is {subtraction(x,y)} )")
    print(f"{x} times {y} is {multiplication(x,y)} ")
    print(f"{x} divided by {y} is {divide(x,y)}")
    print(f"Remainder of dividing {x} by {y} is {remainder(x,y)}")
def square(n):
    return n*n
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b 
def divide(a,b):
    return  a/b
def remainder(a,b):
    return a%b
main()


