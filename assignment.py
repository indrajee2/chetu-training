
# multiplication of a given number

# user=int(input("Enter the number:- "))
# for i in range(1,11):
#     print(f"{user} * {i} = {user*i}")


# *************************************************************

# check the given number is prime or not

# user=int(input("Enter the number :- "))
# count=0
# for i in range(2,user):
#     if user%i==0:
#         count+=1


# if count!=0:
#     print("not prime")
# else:
#     print("prime")


# *****************************************************************

#find  factorial of a given number
user= int(input("Enter the number:- "))
fact=1
for i in range(1,user+1):
    fact=fact*(i)

print(fact)

# **********************************************************************

# print all prime number between given number

user=int(input("Enter the number:- "))

for i in range(2,100):
    count=0
    for j in range(2,i):
            if i%j==0:
                count=1
                break
        
    if count==0:
         print(i)
    

    
            
# *************************************************************************

# sum of digit of a given number

# user=input("Enter only number:-  ")
# s=0
# for i in user:
#     s+=int(i)
# print(s)

# ***********************************************************

# largest among three number

# x=int(input("Enter the value of x:- "))
# y=int(input("Enter the value of y:-  "))
# z=int(input("Enter the vaalue of z:- "))

# if x>y and x>z :
#     print(f"greater number is :- {x}")
# elif y>x and y>z:
#     print(f"greater number is :- {y}")
# else:
#     print(f"greater number is :- {z}")

    
# ***************************************************************************

# print the pattern

# user=int(input("Enter the values:-  "))
# for i in range(user+1):
#     print(i*"* ")

# ******************************************************************************
# check the given string is pelindram or not

# user=input("Enter only strings:-  ")

# reverse=""
# for i in range(len(user)-1,-1,-1):
#     reverse+=user[i]
    

# if reverse==user:
#     print("pelindram")
# else:
#     print("not pelindram")


# 2nd way
# u=input("Enter the string:-  ")
# r=''
# for i in u:
#     r=i+r

# if u==r:
#     print("pelindram")
# else:
#     print("not pelindram")


# ****************************************************************************************
    
# calculate a squre root of a given number using newton's methom
    
# user=eval(input("Enter the number:-  "))
# aprox=0.5*(user)   
# better=0.5*(aprox+user/aprox) 
# while aprox!=better: 
#     aprox=better 
#     better=0.5*(aprox+user/aprox) 

# print(better)











# ********************************************************************************
    
#febonacci series
# 0,1,1,2,3,5,8,13,........
    
# feb=int(input("Enter the number:-  "))

# a=0
# b=1

# for i in range(1,feb+1):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
    


