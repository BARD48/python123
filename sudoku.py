import sys

def file_name_check(file_name):
    # That function checks out file name for that it is valid or unvalid.If it is valid, the functions direct to other functions. Another of task is function directing  to other functions
    if "txt" in file_name:
        direct()
    else: 
        print("Your file name is unvalid")
def direct():
    #That function is opened sudocu txt and read. Function call another functions.
    file=open(f"{sys.argv[1]}","r")
    lines=file.read().strip().split()
    row(lines)
    collum(lines)
    regions(lines)
    solution(lines)
    file.close()
def row(lines):
    #That function makes row lists
    row_set=[]
    for i in range(0,len(lines),9):
        row_set.append([lines[i],lines[i+1],lines[i+2],lines[i+3],lines[i+4],lines[i+5],lines[i+6],lines[i+7],lines[i+8]])
    return row_set
def collum(lines):
    #That function makes collum list
    collum_set=[]
    first_collum_set=[]
    second_collum_set=[]
    third_collum_set=[]
    fourth_collum_set=[]
    fifth_collum_set=[]
    sixth_collum_set=[]
    seventh_collum_set=[]
    eigth_collum_set=[]
    ninth_collum_set=[]
    for i in range(0,len(lines),9):# Numbers of sudocu are appended according to the their collum set 
        if  True:
            first_collum_set.append(lines[i])
        if True:
            second_collum_set.append(lines[i+1])
        if True:
            third_collum_set.append(lines[i+2])
        if True:
            fourth_collum_set.append(lines[i+3])
        if True:
            fifth_collum_set.append(lines[i+4])
        if True:
            sixth_collum_set.append(lines[i+5])
        if True:
            seventh_collum_set.append(lines[i+6])
        if True:
            eigth_collum_set.append(lines[i+7])
        if True:
            ninth_collum_set.append(lines[i+8])
    collum_set.extend([first_collum_set,second_collum_set,third_collum_set,fourth_collum_set,fifth_collum_set,sixth_collum_set,seventh_collum_set,eigth_collum_set,ninth_collum_set])
    return collum_set 
def regions(lines):
    #that function makes region set. And it starts by making top region set,middle region set, bottom region set. After that previous progress repeats left to rigth. Finally previous progress
    # repeats up to the bottom. And there append their regions set
    first_region_set=[]
    second_region_set=[]
    third_region_set=[]
    fourth_region_set=[]
    fifth_regions_set=[]
    sixth_regions_set=[]
    seventh_regions_set=[]
    eigth_regions_set=[]
    ninth_regions_set=[]
    regions_set=[first_region_set,second_region_set,third_region_set,fourth_region_set,fifth_regions_set,sixth_regions_set,seventh_regions_set,eigth_regions_set,ninth_regions_set]
    for i in range(0,3):
        increase_27=27*i
        increase_3=3*i
        for i in range(0,3):
            top_region_set=[]
            middle_region_set=[]
            bottom_region_set=[]

            three_increase=0+(i*3)+increase_27
            one_increase=0+i+increase_3

            for i in range(0+three_increase,3+three_increase):
                if True:
                    top_region_set.append(lines[i])
                if True:
                    middle_region_set.append(lines[i+9])
                if True:
                    bottom_region_set.append(lines[i+18])

            regions_set[one_increase].extend(top_region_set)
            regions_set[one_increase].extend(middle_region_set)
            regions_set[one_increase].extend(bottom_region_set)
    return (regions_set)
def solution(lines):
    #The functon solve problem and the functıon write on the output txt
    regions_set=regions(lines)
    collum_set=collum(lines)
    row_set=row(lines)
    possible_solutions=["1","2","3","4","5","6","7","8","9"] 
    new_lines=[]
    for new_line in row_set:
        new_lines.extend(new_line)
        step_number=0
    len_number_zero=new_lines.count("0") #It ıs for finding that how many solution there
    while step_number!=len_number_zero: 
        step_number+=1
        solution_found=False
        while "0" in new_lines and not solution_found: #It checks 0 which it is there or isn't there
            for k in range(0,3):
                increase_27_thing=27*k
                for j in range(0,3):
                    nine_increase=9*j+increase_27_thing 
                    for n in range(0+nine_increase,9+nine_increase):#It is is for increase index number for sudocu lines
                        a=n%9 #It is index number of row set which it is for solution
                        b=n//3-3*j-6*k #it is index number of region set which it is for solution
                        c=n//9  #It is index number of colllum set which it is for solution
                        if new_lines[n]=="0":
                            collum_number=(n%9)+1
                            row_number=(n//9)+1
                            values_set=[]
                            for i in range(0,9): #That for loop checks ıt is solution or not
                                value= ( possible_solutions[i] in collum_set[a]) or ( (possible_solutions[i]) in regions_set[b]) or (possible_solutions[i] in row_set[c])
                                if value==False:
                                    values_set.append([step_number,row_number,collum_number,possible_solutions[i]])
                                else:
                                    pass 
                            solutions=[]
                            if solution_found: #It is for solving problem respectively. That logic like jumpn logic on assembly
                                break
                            elif len(values_set)==1: #It is for one solution
                                    solutions.extend(values_set)
                                    if len(solutions)==1: #It changes region set list,row list ,collum list to according to solution
                                        new_lines[n]=solutions[0][3]
                                        collum_set[a][n//9]=solutions[0][3]
                                        regions_set[b][(n%3)+3*j]=solutions[0][3]
                                        row_set[c][n%9]=solutions[0][3]
                                        explaining_line=(f"{(18 *'-')}\nStep {solutions[0][0]} {'-'} {int(solutions[0][3])} {'@'} R{solutions[0][1]}C{solutions[0][2]}\n{(18*'-')}")
                                        row_lines_second=[]
                                        for m in range(0,9):
                                            r=[]
                                            for n in range(0,9): # It is for remove the comma on the rows
                                                r.append(new_lines[n+9*m])
                                                row_line=" ".join(r)
                                            row_lines_second.append(row_line)
                                        solution_found=True
                                        if step_number==1:
                                            file=(f"{sys.argv[2]}","w")
                                            file=open(f"{sys.argv[2]}","w")
                                            file.write(explaining_line) #That is for explaining line
                                            file.write("\n")
                                            for line in row_lines_second: #That loop write solution line by line on output txt
                                                file.write(line)
                                                file.write("\n")
                                            file.close()
                                        elif step_number>1: 
                                            file=open(f"{sys.argv[2]}","a")
                                            file.write(explaining_line)
                                            file.write("\n") #It is for writing another line
                                            for line in row_lines_second:
                                                file.write(line)
                                                file.write("\n")
                                            file.close() 
                                        if step_number==len_number_zero: # It is for add last line
                                                    file=open(f"{sys.argv[2]}","a")
                                                    file.write(f"{18*'-'}")
                                                    file.close()                        
def main():
    file_name_check(sys.argv[1])
if __name__ =="__main__":
    main()    