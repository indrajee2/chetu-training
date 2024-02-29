# Find the size of a Set in Python
# s={12,23,43,4,24.45,56,34,"indra","ad","chore",123,45}
# count=0
# for i in s:
#     count+=1


# print(count)


# Iterate over a set in Python
# s={12,23,43,4,24.45,56,34,123,45}
# a=set([12,23,34,5,2,2,1,3,5,6,12,7,7,7,5,456,546,34,5,45,4,65,])
# for i in s:
#     print(i)



# Python – Maximum and Minimum in a Set
# mi=min(s)
# ma=max(s)
# short=sorted(s)
# uni=s.union(a)
# inter=s.intersection(a)
# diff=s.difference(a)
# u=s|a
# i=s&a
# d=s-a
# print("minimum :- ",mi)
# print("maximum",ma)
# print(short)
# print("union of the set",uni)
# print("difference of two set",diff)
# print("intersection:-" ,inter)
# print(u)
# print(i)
# print(d)



# Python – Remove items from Set

# s.remove(24.45)
# s.discard(34)
# while s:
#     s.discard(next(iter(s)))
#     print(s)
#     # Python – Check if two lists have at-least one element common


# Python program to find common elements in three lists using sets
# set1={12,23,34,66,78,45,4,55,6,234,7,8,234,79,8,76,54,234,3,2,2,2,332,234,45,657,666,54,32,2,3445565,5655,432,234,4565,5432,3243545,521,2334,565,5543,35,6554,33,4455,543,45,43,}
# set2={234,2,332,234,45,657,666,54,32,2,3445565,5655,432,234,4565,5432,3243545,521,2334,565,5543,35,6554,33,4455,543,45,43,}
# set3={1,2,332,234,45,657,666,54,32,2,3445565,5655,432,234,4565,5432}
# set4=set1.intersection(set2)
# set5=set4.intersection(set3)
# print(set5)
# print(set4)


# Python – Find missing and additional values in two lists
# s1=[12,23,34,45,56,67,7]
# s2=[12,3,4,5,6,67,78,89,9]
# s3=set(s2)-set(s1)

# print("missing values of s1:- ",s3)
# print("additional valuse of s1",set(s1)-set(s2))
# print("missing values of s2:- ",set(s1)-set(s2))
# print("additional valuse of s1",set(s2)-set(s1))


# Python program to find the difference between two lists

# s1=[12,23,34,45,56,67,7]
# s2=[12,3,4,5,6,67,78,89,9]
# s3=set(s1)-set(s2)
# print('Difference of s1 and s2:- ',s3)

# Python Set difference to find lost element from a duplicated array
# a=set([1,2,3,4,5,6,7])
# b=set([2,3,4,5,6,7,8,9])
# c=b-a
# print("missing values from first list:- ",list(c))
# print("missing element from second list:-" ,list(a-b))

# Python program to count number of vowels using sets in given string

# s="indrajeet kumar"
# a=set("aeiouAEIOU")
# count=0
# for i in s:
#     if i in a:
#         count+=1

# print(count)

# Concatenated string with uncommon characters in Python

# a=input("Enter first string:- ")
# b=input("Enter second string:- ")
# c=set(a)
# d=set(b)
# e=list(c^d)  
# print(" ".join(e))



# Python – Program to accept the strings which contains all vowels

# user=input("Enter the strings:- ")
# vol=set("aeiou")
# s=""
# st=set(s)
# for i in user:
#     if i in vol:
#         s+=i
#     # print(s)
# if len(s)==len(vol):
#     print("accepted")
# else: 
#     print("not accepted")
        

# Python – Check if a given string is binary string or not


b=input("Enter the binary string:- ")
c=""
for i in b:
    if int(i)==0 or int(i)==1:
        c+=str(i)    
        
if len(c)==len(b):
    print("yes given string is binary ")
    
else:
        print("no accepted")
    



# Python set to check if string is panagram




# Python Set – Pairs of complete strings in two sets



# Python program to check whether a given string is Heterogram or not



