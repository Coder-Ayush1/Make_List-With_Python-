a = int(input("No. of items needed to stored: "))

lis = []

n = 1

while(a>0) :
   str = input(f"Item {n}: ") 
   lis.append(str)
   a = a-1 
   n = n + 1

lis.sort()
print(lis)

input("Press enter to exit....")
