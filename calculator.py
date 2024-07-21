import sys

#That checks index error.
file=open(f"{sys.argv[2]}","a")
if len(sys.argv)!=3:
    file.write("ERROR: This program needs to two command line arguments to run, where first one is the input file and the second one is the output file!")
    sys.exit()
if len(sys.argv)==3:
    pass
def cleaner():
    #That function checks error.
    try:
        print("Program is going to terminate")
        with open (f"{sys.argv[1]}","r") as file:
            read=file.read().strip().split("\n")
            a=[]
            for i in read: #That loop for clean the space
                if i=="" or i.strip()=="":
                    continue
                else:
                    a.append(i.strip(" ").split())
            print(a)
            for chars in a:
                
                length=len(chars) #Tha if else statements are for special case
                if chars==["ERROR"]: 
                    string("ERROR")
                if chars==['There', 'is', 'nothing']:
                    string("There is nothing")
                try:
                    assert length==3
                    for l in range(length):
                            z,x,y=0,0,0
                            if l==0:
                                fake=chars[l]
                                try: #That checks first first operand error
                                    if "." in chars[l]:
                                        first_operand=float(chars[l])
                                    else:
                                        first_operand=int(chars[l])
                                except ValueError:
                                    z=1
                                    name="ERROR: First operand is not a number!"
                            elif l==1: #That checks operator error
                                fake1=chars[l]
                                try:
                                    operator=chars[l]
                                    assert chars[l] in ["+","-","*","/"]
                                except AssertionError: 
                                    x=2
                                    name="ERROR: There is no such an operator!"
                            elif l==2: #That checks second operator
                                fake2=chars[l]
                                try:
                                    if "." in chars[l]: #That if else statement is for finding which one is integer which one is float
                                        second_operand=float(chars[l])
                                    else:
                                        second_operand=int(chars[l])
                                except ValueError:
                                    y=3
                                    name="ERROR: Second operand is not a number!"
                    if x==0 and z==0 and y==3:
                        write_2(name,first_operand,operator,fake2)
                    elif x==2 and y==0 and z==0:
                        write_2(name,first_operand,fake1,second_operand)
                    elif z==1 and x==0 and y==0:
                        write_2(name,fake,operator,second_operand)
                    
                    elif operator=="+":   #That  if else statements are for calculating values
                        result=(first_operand+second_operand)
                        value=f"{result:.2f}"
                        write(first_operand,operator,second_operand,value)
                    elif operator=="/":
                        result=first_operand/second_operand
                        value=f"{result:.2f}"
                        write(first_operand,operator,second_operand,value)
                    elif operator=="-":
                        result=first_operand-second_operand
                        value=f"{result:.2f}"
                        write(first_operand,operator,second_operand,value)
                    elif operator=="*":
                        result=first_operand*second_operand
                        value=f"{result:.2f}"
                        write(first_operand,operator,second_operand,value)
                except AssertionError:
                        string("ERROR: Line format is errorneous!")
    except FileNotFoundError:
        file.write(f"Error: There is either no such file namely {sys.argv[1]} or this program does not have permission to read it")
def string(thing):
    #That functions write on txt that string errors
    with open(f"{sys.argv[2]}","a") as file:
        file.write(thing)
        file.write("\n")
def write(first_operand,operator,second_operand,value):
        #That function write on txt that values and operations
        with open(f"{sys.argv[2]}","a") as file:
            if operator=="+":
                file.write(f"{first_operand} + {second_operand}")
                file.write("\n")
                file.write(f"={value}")
                file.write("\n")
            elif operator=="/":
                file.write(f"{first_operand} / {second_operand}")
                file.write("\n")
                file.write(f"={value}")
                file.write("\n")
            elif operator=="*":
                file.write(f"{first_operand} * {second_operand}")
                file.write("\n")
                file.write(f"={value}")
                file.write("\n")
            elif operator=="-":
                file.write(f"{first_operand} - {second_operand}")
                file.write("\n")
                file.write(f"={value}")
                file.write("\n")
def write_2(name,x,y,z):
    with open(f"{sys.argv[2]}","a") as file:
        file.write(f"{x} {y} {z}")
        file.write("\n")
        file.write(name)
        file.write("\n")
def main(): 
    cleaner()
if __name__ =="__main__":
    main()    