n=5
for i in range(n):
    for j in range(2*n-1):
        print(end=" ")
        
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#         *
#       * *
#     * * *
#   * * * *
for i in range(n):
    for j in range(n-i):
        print(end=" ")
        
    for j in range(i):
        print("*",end=" ")
    print() 


# for i in range(n):
#     for j in range(n-i-1):
#         print(end=" ")
        
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    
    
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(end=" ")
        
#     for j in range(i-1):
#         print("*",end=" ")
#     print()
        
    
    
# user= int(input("Enter the number:- "))
# for i in range(user):
#     for j in range(user-i-1):
#         print(end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    

# row=5
# for i in range(row):
#     print((row-i-1)*" "+"* "*(i+1))
    
# for j in range(row,0,-1):
#     print((row-j)*" "+"* "*(j))

# for c
# for i in range(row):
#     for j in range(row):
#         if (i==0 or i==4 and (j>0)) or j==0 :
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()

# for D
# row=5
# for i in range(row):
#     for j in range(row):
#         if  j==1 or (i==0 or i==4) and (j>0 and j<4) or (j==4 and i!=0 and i!=4):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()

def pattern(n):
    for i in range(n):
        for j in range(n-1):
            print(end=" ")
        for j in range(i):
            print("@",end=" ")
        print()
        
pattern(5)