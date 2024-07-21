N=int(input("Please enter number: "))
Sum_off_odd_numbers=0
Sum_off_even_numbers=0
Total_off_even_numbers=0
It_is_for_one=1
for i in range(1,N+1):

    if i % 2==1:
        Sum_off_odd_numbers+=i
    elif i % 2==0:
        Sum_off_even_numbers+=i
        Total_off_even_numbers+=1
if N==1:
    Average_even_numbers=   "You don't have any number for sum up"
else:
    Average_even_numbers=Sum_off_even_numbers/Total_off_even_numbers  
  
print(f"Sum off odd number is {Sum_off_odd_numbers} . Average even numbers {Average_even_numbers}")

