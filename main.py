a = int(input("No. of items needed to stored: ")) #take input that how many items are needed

lis = []

n = 1

while(a>0) :    #by while loop instead of 
   str = input(f"Item {n}: ")    #create a loop to take input accoring to a
   lis.append(str)
   a = a-1 
   n = n + 1

lis.sort() #sort list alphabeticaly ( a ,b ,c)
print(lis) #print the sorted list.

input("Press enter to exit....") #pause the terminal until any key is pressed(input is given)

