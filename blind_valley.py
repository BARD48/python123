import sys
def deep_copy(lst, copies=None):
    #This function was written as an alternative to deep copy because deep copy can cause slowness.So that function include list part only
    if copies is None:
        copies = {}

    if id(lst) in copies:
        return copies[id(lst)]

    if not isinstance(lst, list):
        return lst  

    copied_list = []
    copies[id(lst)] = copied_list

    for item in lst:
        copied_list.append(deep_copy(item, copies))

    return copied_list
def read():
    #That function makes row_set and make fake list which have first row_set information like "L" or "R"
    #That function find x and y and assign information about constraints to variables like upward side and left side
    with open(sys.argv[1],"r") as f:
        left_side=f.readline().split()
        right_side=f.readline().split()
        upward_side=f.readline().split()
        downward_side=f.readline().split()
        row_set=[]
        for row in f.readlines():
            row_set.append(row.split())
        y=(len(row_set))
        x=(len(row_set[0]))
        fake_list=deep_copy(row_set)
        return x,y,fake_list,left_side,right_side,upward_side,downward_side,row_set
def solve():
    x,y,fake_list,left_side,right_side,upward_side,downward_side,row_set=read()
    i=0
    j=0
    index=0
    control_list=[]
    possible_solution=[["H","B"],["B","H"],["N","N"]]
    def solution(i,j,row_set,index,possible_solution,control_list,x,y):
            def control(i,j,row_set,x,y,eleman):
                #That function checks whether h and b are neighbors
                #That function checks left and up side mostly when placing ["H","B"],["B","H"],"["N","N"]" except in special cases.It returns false if they are neighbors when you place
                if fake_list[i][j]=="L":
                    if i==0 and j==0:
                        if fake_list[i][j]=="L":
                            return True
                    elif i==0 and j<x: #That condition statement checks left side
                        if row_set[i][j-1]=="H" and eleman[0]=="H":
                            return False
                        elif row_set[i][j-1]=="B" and eleman[0]=="B":
                            return False
                        else:
                            return True
                    elif i!=0 and j==0 : 
                        if j+2<x:
                            if fake_list[i][j+2]=="D":# That condition statement checks top of R whether h and b are neighbors.
                                if row_set[i][j+2]=="H" and eleman[1]=="H":
                                    return False
                                elif row_set[i][j+2]=="B" and eleman[1]=="B":
                                    return False
                        if i>1:
                            if fake_list[i-1][j+1]=="D": #That condition statement checks The rigth side of R whether h and b are neighbors.
                                if row_set[i-1][j+1]=="H" and eleman[1]=="H":
                                    return False
                                elif row_set[i-1][j+1]=="B" and eleman[1]=="B":
                                    return False
                        if row_set[i-1][j]=="H" and eleman[0]=="H" : #The condition statement checks up side
                            return False
                        elif row_set[i-1][j]=="B" and eleman[0]=="B": 
                            return False
                        else:
                            return True
                    elif i!=0 and j<x:
                        if j+2<x:
                            if fake_list[i][j+2]=="D":# That condition statement checks top of R whether h and b are neighbors.
                                if row_set[i][j+2]=="H" and eleman[1]=="H":
                                    return False
                                elif row_set[i][j+2]=="B" and eleman[1]=="B":
                                    return False
                        if i>1:
                            if fake_list[i-1][j+1]=="D":#That condition statement checks The rigth side of R whether h and b are neighbors.
                                if row_set[i-1][j+1]=="H" and eleman[1]=="H":
                                    return False
                                elif row_set[i-1][j+1]=="B" and eleman[1]=="B":
                                    return False
                        if row_set[i][j-1]=="H" and eleman[0]=="H": #The condition statements checks up side and left side
                            return False
                        elif row_set[i-1][j]=="H" and eleman[0]=="H":
                            return False
                        elif row_set[i][j-1]=="B" and eleman[0]=="B":
                            return False
                        elif row_set[i-1][j]=="B" and eleman[0]=="B":
                            return False
                        else:
                            return True
                elif fake_list[i][j]=="U":
                    if i==0 and j==0:
                        if fake_list[i][j]=="U":
                            return True
                    elif i==0 and j<x: ##That condition statement checks left side
                        if row_set[i][j-1]=="H" and eleman[0]=="H":
                            return False
                        elif row_set[i][j-1]=="B" and eleman[0]=="B":
                            return False
                        else:
                            return True
                    elif i!=0 and j==0:
                        if j+1<x:
                            if fake_list[i][j+1]=="D":#That condition statement checks The rigth side of U whether h and b are neighbors.
                                if row_set[i][j+1]=="H" and eleman[0]=="H":
                                    return False
                                elif row_set[i][j+1]=="B" and eleman[0]=="B":
                                    return False
                        if row_set[i-1][j]=="H" and eleman[0]=="H":#The condition statement checks up side
                            return False
                        if row_set[i-1][j]=="B" and eleman[0]=="B":
                            return False
                        if row_set[i-2][j]=="H" and eleman[0]=="B":
                            return False 
                        elif row_set[i-2][j]=="B" and eleman[0]=="H":
                            return False
                        else:
                            return True
                    elif i!=0 and j<x:
                        if j+1<x:
                            if fake_list[i][j+1]=="D": #That condition statement checks The rigth side of U whether h and b are neighbors.
                                if row_set[i][j+1]=="H" and eleman[0]=="H":
                                    return False
                                elif row_set[i][j+1]=="B" and eleman[0]=="B":
                                    return False
                        if row_set[i][j-1]=="H" and eleman[0]=="H":#The condition statements checks up side and left side
                            return False
                        elif row_set[i][j-1]=="B" and eleman[0]=="B":
                            return False
                        elif row_set[i-1][j]=="H" and eleman[0]=="H":
                            return False
                        elif row_set[i-1][j]=="B" and eleman[0]=="B":
                            return False
                        else:
                            return True
                elif fake_list[i][j]=="D":
                    if row_set[i][j-1]=="H" and eleman[0]=="H":
                        return False
                    elif row_set[i][j-1]=="B" and eleman[0]=="B":
                        return False
                    elif row_set[i-1][j]=="H" and eleman[0]=="H":
                            return False
                    elif row_set[i-1][j]=="B" and eleman[0]=="B":
                            return False
                    else:
                        return True
                    
            def finish(row_set):
                #That function for No solution case.It is checks whether rowset have full of "N".
                if all(all(cell == 'N' for cell in row) for row in row_set):
                    write1()
                    sys.exit()       
            if index == ((x*y)//2):
                #It call function and checks tiles number is enough
                control_list.append(row_set.copy())
                game=found(row_set,x,y,left_side,right_side,upward_side,downward_side)
                if game==False:
                    finish(row_set)
                    return 
                else:
                    write2(row_set)
                    sys.exit()#It is for stop the program
            for eleman in possible_solution:
                    #It calls control function by eleman. If control returns true ,It does the following operations accordingly
                    if control(i,j,row_set,x,y,eleman)==True:
                        if fake_list[i][j]=="L":
                            #It put on new values according to the eleman on row set
                            row_set[i][j] = eleman[0]
                            row_set[i][j+1]=eleman[1]
                            if j+2==x:
                                if i+1!=y:
                                    #It is for pass next line.
                                    solution(i+1,0,row_set, index + 1, possible_solution, control_list,x,y)
                                elif i+1==y:
                                    solution(i,j+2,row_set, index + 1, possible_solution, control_list,x,y)     
                            else:
                                
                                solution(i,j+2,row_set, index + 1, possible_solution, control_list,x,y)
                        elif fake_list[i][j]=="U":
                            #It put on new values according to the eleman on row set
                            row_set[i][j]=eleman[0]
                            row_set[i+1][j]=eleman[1]
                            if j+1==x:
                                if i+1!=y:
                                    #It is for pass next line.
                                    solution(i+1,0,row_set, index + 1, possible_solution, control_list,x,y)
                                elif i+1==y:
                                    solution(i,j+1,row_set, index + 1, possible_solution, control_list,x,y)
                            else:
                                solution(i,j+1,row_set, index + 1, possible_solution, control_list,x,y)
                        elif fake_list[i][j]=="D":
                            if j+1==x:
                                if i+1!=y:
                                    #It is for pass next line.
                                    solution(i+1,0,row_set, index, possible_solution, control_list,x,y)
                                    break
                                    
                                elif i+1==y:
                                        solution(i,j+1,row_set, index, possible_solution, control_list,x,y)
                                        break
                                        
                            else:
                                solution(i,j+1,row_set, index, possible_solution, control_list,x,y)
                                break
                                
    solution(i,j,row_set, index, possible_solution, control_list,x,y)
def found(row_set,x,y,left_side,right_side,upward_side,downward_side):
    #If it determines the high and base numbers according to left_side right side ,upward side ,downward side. It checks by row and collum so It makes collums 
    collum_set=[]
    for i in range(x):
        collum=[row[i] for row in row_set]
        collum_set.append(collum)
    left=True
    for i in range(len(left_side)):
        if "-1"==left_side[i] and row_set[i]!=["L"] and row_set[i]!=["R"] and row_set[i]!=["U"] and row_set[i]!=["D"]:
            left=True
            continue
        elif row_set[i].count("H")==int(left_side[i]) and row_set[i]!=["L"] and row_set[i]!=["R"] and row_set[i]!=["U"] and row_set[i]!=["D"]:
            left=True
        else:
            left=False
            break
    right=True      
    for i in range(len(right_side)):
        if "-1"==right_side[i] and row_set[i]!=["L"] and row_set[i]!=["R"] and row_set[i]!=["U"] and row_set[i]!=["D"]:
            right=True
            continue
        elif row_set[i].count("B")==int(right_side[i]) and row_set[i]!=["L"] and row_set[i]!=["R"] and row_set[i]!=["U"] and row_set[i]!=["D"]:
            right=True
        else:
            right=False
            break
    upward=True
    for j in range(len(upward_side)):
        if "-1"==upward_side[j]:
           if collum_set[j]!=["U"] and collum_set[j]!=["L"] and collum_set[j]!=["R"] and collum_set[j]!=["D"]:
                upward=True
                continue
           else:
               upward=False
               break
        
        elif collum_set[j].count("H")==int(upward_side[j]):
            if collum_set[j]!=["U"] and collum_set[j]!=["L"] and collum_set[j]!=["R"] and collum_set[j]!=["D"]:
                upward=True
                continue
            else:
                upward=False
                break
        else:
            upward=False
            break
    downward=True
    for j in range(len(downward_side)):
        if "-1"==downward_side[j]:
            if collum_set[j]!=["U"] and collum_set[j]!=["L"] and collum_set[j]!=["R"] and collum_set[j]!=["D"]:
                downward=True
                continue
            else:
                downward=False
                break
        elif collum_set[j].count("B")==int(downward_side[j]):
               if collum_set[j]!=["U"] and collum_set[j]!=["L"] and collum_set[j]!=["R"] and collum_set[j]!=["D"]:
                downward=True
                continue
               else:
                   downward=False
                   break
        else:
            downward=False
            break
    if downward and upward and left and right:#If all o them true return true
        return True
    else:
        return False
def write1():
    #That function write no solution part
    with open(sys.argv[2],"w") as f:
        f.write("No solution!")
def write2(row_set):
    #That function write solution line by line
    with open(sys.argv[2],"a") as f:
        a=0
        for row in row_set:
           if a>0:
            f.write("\n")
           a+=1
           c=0
           for i in row:
               c+=1
               f.write(i)
               if c<len(row):
                f.write(" ")
def main():
    read()
    solve()

if __name__ == "__main__":
    main()
