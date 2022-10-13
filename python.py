lowerVal=int(input("Enter the lower range:"))
upperVal=int(input("Enter the upper range:"))
number=int(input("Enter the number to be divided by:"))
for j in range (lowerVal,upperVal+1):
    if(j%number==0):
     print(j)