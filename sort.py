import sys
def bubble(filename):
    file=open(f"{filename}" ,"r") #It reads txt file    
    number_list=file.read().strip().split()
    len_number_list=len(number_list)
    for i in range(0,len_number_list): #It transforms string to integer number
        number_list[i]=int(number_list[i])
    number=0
    while number!=len_number_list-1:
        number+=1
        sorted_number=True
        for i in range(len_number_list-1): # The function checks each pair number
            if number_list[i]<=number_list[i+1]:
                pass
        
            elif number_list[i]>number_list[i+1]: # The function changes number_list2 and number_list1 according to their index number
                number_list[i],number_list[i+1]=number_list[i+1],number_list[i]
                sorted_number=False
              
             
        formatted_integer = ' '.join(map(str, number_list)) #It provides space between two numberd
        step=(f"Pass {number}: {formatted_integer} ") #It gives information about solution
        if sorted_number:
            break
        elif number==1:
            file=open(f"{sys.argv[2]}","x")   #It opens new file and writes inside about step
            file=open(f"{sys.argv[2]}","w")
            file.write(step)
            file.write("\n")
            file.close()
        elif number<len_number_list:
            file=open(f"{sys.argv[2]}","a") #It adds information about step
            file.write(step)
            file.write("\n")
            file.close()


def insertion_sort(filename):
    file=open(f"{filename}","r")
    number_list=file.read().strip().split()
    for i in range(0,len(number_list)):
        number_list[i]=int(number_list[i])
    step_number=0   
    for index in range(1, len(number_list)):
        step_number+=1 #ıt is for calculate step number
        pos= index-1
        while pos>=0: #ıt check number that condition 
            if number_list[pos]>number_list[index]:   #It places to smallest number to the left acording to the current index number
                number_list.insert(pos,number_list[index])  
                number_list.pop(pos+2)
                pos=pos-1
                index=index-1
            elif number_list[pos]<= number_list[index]: #It is part of functıon task
                pos=pos-1
                index=index-1
                pass
        
        formatted_integer = ' '.join(map(str, number_list)) #It is for remove comma
        step=(f"Pass {step_number}: {formatted_integer} ") #It includes ınstructions about step
        print(step)
        if index==1:
            print(i)
            file=open(f"{sys.argv[3]}","x") #It opens new file 
            file=open(f"{sys.argv[3]}","w")
            file.write(step)
            file.write("\n")
            file.close()
        elif index<len(number_list):
            file=open(f"{sys.argv[3]}","a") 
            file.write(step)
            file.write("\n")
            file.close()
def main():
    bubble(sys.argv[1])
    insertion_sort(sys.argv[1])
if __name__=="__main__":
    main()