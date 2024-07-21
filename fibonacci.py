import sys 
def read(): 
    with open (f"{sys.argv[1]}","r") as file:
        arr=file.read().split()
        c=0
        for i in arr:
            write(int(i),c) #It is for call function again
            result=naive_fib(int(i))
            d=len(arr)
            if int(i)>0:
                write_last(int(i),result,c,d) 
            c+=1
def naive_fib(n):
    try:
        assert n>0
        if n>2:
            fib,fib1,fib2=thing(n)
            sentence=fib+" "+"="+" "+fib1+" "+"+"+" "+fib2
            write_middle(sentence)
            return naive_fib(n-1)+naive_fib(n-2)
        elif n==1 or n==2:
            fib,fib1,fib2=thing(n)
            sentence=fib+" "+"="+" "f"{1}"
            write_middle(sentence)
            return 1
    except AssertionError:
        #It is for negative and 0 case
        with open (f"{sys.argv[2]}","a") as file:
            file.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!")
            file.write("\n")
            file.write(f"{str(n)+'.'} Fibonacci number is: nan")
            file.write("\n")
def write(n,c):
    if c==0: #The function can't write over over again. It is write once
        with open (f"{sys.argv[2]}","w") as file:
            file.write(f"{32*'-'}")
            file.write("\n")
            file.write(f"Calculating {str(n)+'.'} Fibonacci number:""\n")
    else:
        with open (f"{sys.argv[2]}","a") as file:
            file.write(f"{32*'-'}")
            file.write("\n")
            file.write(f"Calculating {str(n)+'.'} Fibonacci number:""\n")
def write_middle(sentence):
    #It is for writing sentence file
    with open (f"{sys.argv[2]}","a") as file:
        file.write(sentence)
        file.write("\n")
def thing(n):
    fib=f"fib({n})" #It ıs for string version of functon 
    fib1,fib2=None,None
    if n>2:
        fib1=f"fib({n-1})"

        fib2=f"fib({n-2})"
    return fib,fib1,fib2 
def write_last(n,result,c,d): #ıt is for write last part
    with open (f"{sys.argv[2]}","a") as file:
        
        file.write(f"{str(n)+'.'} Fibonacci number is: {result}")
        file.write("\n")
        if c==d-1:
            file.write(f"{32*'-'}")
def read2(): 
    with open (f"{sys.argv[1]}","r") as file:
        arr=file.read().split()
        c=0
        for i in arr:
            write2(int(i),c) #It is for call function again
            result=eager(int(i))
            d=len(arr)
            if int(i)>0:
                write_last2(int(i),result,c,d)   
            c+=1
eager_list=[]
def eager(n):
    global eager_list
    k=len(eager_list)
    try:
        assert n>0
        if n==1:
            fib,fib1,fib2=thing2(n)
            sentence=fib+" "+"="+" "f"{1}"
            write2_middle(sentence)
            if k<2:
                eager_list.append(1)
            return 1
        elif n==2:
            fib,fib1,fib2=thing2(n)
            sentence=fib+" "+"="+" "f"{1}"
            write2_middle(sentence)
            if k<2:
                eager_list.append(1)
            return 1
        elif n>2:
            try:
                value=eager_list[n-1] 
                fib,fib1,fib2=thing2(n)
                sentence=fib+" "+"="+" "f"{value}"
                write2_middle(sentence)
                return value

            except IndexError:
                fib,fib1,fib2=thing2(n)
                sentence=fib+" "+"="+" "+fib1+" "+"+"+" "+fib2
                write2_middle(sentence)
                value=eager_list[n-2]+eager_list[n-3]
                return eager(n-1)+eager(n-2)
            finally:
                try:
                    value=eager_list[n-2]+eager_list[n-3]
                    
                    if len(eager_list)<n:
                        eager_list.append(value)
                    return value
                except IndexError:
                    return eager(n-1)+eager(n-2)
                finally:
                    value=eager_list[n-2]+eager_list[n-3]
                    if len(eager_list)<n:
                        eager_list.append(value)
                    return value         
    except AssertionError:
            f=open(sys.argv[3],'a')
            f.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
            f.write(f"{str(n)+'.'} Fibonnacci Number is: nan\n")
def write2(n,c):
    f=open(sys.argv[3],'a')
    f.write(f"{32*'-'}\n")
    f.write(f"Calculating {str(n)+'.'} Fibonacci number:\n")
    f.close()
def write2_middle(sentence):
    f=open(sys.argv[3],'a')
    f.write(sentence)
    f.write("\n")
    f.close()
def thing2(n):
    fib=f"fib({n})" #It ıs for string version of functon 
    fib1=f"fib({n-1})"
    fib2=f"fib({n-2})"
    return fib,fib1,fib2 
def write_last2(n,value,c,d):
    f=open(sys.argv[3],'a')
    f.write(f"{str(n)+'.'} Fibonacci number is: {value}\n")
    if c==d-1:
        f.write(f"{32*'-'}\n")
        f.write("Structure for the eager solution:\n")
        f.write(f"{eager_list}\n")
        f.write(f"{32*'-'}")
    f.close()
def main():
   read()
   read2()

if __name__ == "__main__":
    main()


