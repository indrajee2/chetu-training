
# Example 1: Print the first 10 natural numbers using for loop.
# for i in range(1,10+1):
#     print(i)


# Example 2: Python program to print all the even numbers within the given range.

# a=int(input("Enter the first value:- "))
# b=int(input("Enter the second value:-  "))

# for i in range(a,b):
#     if i%2==0:
           
#         print(f"Even {i}")
    
   
    
# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
# user=int(input("Enter the number:- "))
# cal=0
# for i in range(1,user+1):
#     cal+=i
# print(cal)
    
# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# cal=0
# a=int(input("Enter the number"))
# for i in range(1,a):
#     if i%2==0:
#         pass
#     else:
#         cal+=i

# print(cal)
# Example 5: Python program to print a multiplication table of a given number

# user=int(input("Enter the number:- "))
# for i in range(1,11):
#     print(user*i)


# Example 6: Python program to display numbers from a list using a for loop.


# a=[10,20,40,50]
# for i in a:
#     print(i)


# Example 7: Python program to count the total number of digits in a number.

# user=(input("Enter the number:-  "))

# count=0
# for i in user:
#     count+=1

# print(count)

# Example 8: Python program to check if the given string is a palindrome.


# user=(input("Enter the string:-  "))

# reverse=user[::-1]
# if reverse == user:
#     print("pelindrome")
# else:
#     print("not pelindrome")


# Example 9: Python program that accepts a word from the user and reverses it.


# user=input("Enter the string:- ")
# rev=""
# for i in user:
#     rev=i+rev

# print(rev)


# Example 10: Python program to check if a given number is an Armstrong number.




# Example 11: Python program to count the number of even and odd numbers from a series of numbers.

# user=int(input("Enter the number:- "))
# even_count=0
# odd_count=0
# for i in range(user):
#     if i%2==0:
#         print(i)
#         even_count+=1
#     else:
#         # print("odd")
#         odd_count+=1

# print(f"Total number of evan is {even_count}")
# print(f"Total number of odd is {odd_count}")



# Example 12: Python program to display all numbers within a range except the prime numbers.


# a=int(input("Enter the number:- "))
# for i in range(2,a+1):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             print(i)
        
        
# Example 13: Python program to get the Fibonacci series between 0 to 50.

# a=0
# b=1

# for i in range(50):
#     print(a)
#     c=a+b
#     a,b=b,c


    
# Example 14: Python program to find the factorial of a given number.
"""
a=0
b=1
user=int(input("Enter the number:- "))
for i in range(user):
    c=a+b
    a,b=b,c

print(a)

"""


# Example 15: Python program that accepts a string and calculates the number of digits and letters.
# user=input("Enter the values:- ")
# digit=0
# letter=''
# for i in user:
#     if i.isdigit():
#         digit+=int(i)
#     elif i.isalpha():
#         letter+=i
# print(digit)
# print(letter)







# Example 16: Python program to check the validity of password input by users.

# passwrd=input("Enter the strong password:-   ")
# char=False
# spec=False
# uppers=False

# if len(passwrd)>=8 and len(passwrd)<=20:

#     for i in passwrd:
#         if i.isalnum():
#             char=True
#         elif i=="@" or i=="#" or i=="&" or i=="-" or i=="_" or i=="$" or i=="%" or i=="`":
#             spec=True
        

        
#     if char==True and spec==True :
#         print(f"congratulation you have a strong passworld ")
#         print(passwrd)
#     else:
#         print("Enter strong password.........")






# Example 17: Python program to convert the month name to a number of days.*

# m_list=['january',"february","march","april","may","june","july","august","september","october","november","december"]
# for i in m_list:
#     if i=="february":
#         print("days  28/ 29for leap year")
#     elif i=="january" or i=="march" or i=="may" or i=="july" or i=="august" or i=="october" or i=="december":
#         print("days 31" )
#     else:
#         print("days 30")





#swapping 3 variable without using any extra vaeriable


# a=eval(input("A:- "))
# b=eval(input("B :- "))
# c=int(input("C :- "))
# a=a+b+c
# b=a-(b+c)
# c=a-(b+c)
# a=a-(b+c)
# print(a,b,c)
a=[12,34,55,56,3,23,56,78]
count=[]
for i in range(len(a)-1,0,-1):
    count.append(a[i])
print(count)

# remove empty list from a list

a=[12,[],4,[],34,46,[],[],245,[],23,56,65,[]]
for i in range(a.count([])):
    del a[a.index([])]
    
    
        
print(a)

# remove duplicates form list/

listt=[12,23,234,53,23,1,23,3,345]
def duplicate(lists):
    a=[]
    for i in range(len(listt)):
        if listt[i] not in a:
            a.append(listt[i])
                
    print(a)
    
# calling the function
duplicate(listt)


ab=[]
for i in listt:
    if i not in  ab:
        ab.append(i)
        
print(ab)


a=list(set(listt))
print(a)


# list comprehesive