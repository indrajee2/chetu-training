
# 1. Write a Python program to find the union of two sets without using the union() method.
'''

a={1,2,3,5,6,5,6,4}
b={9,8,7,6,5,4,3,2}

for i in a:
    if i not in b:
        b.add(i)
        
print(b)

'''
# 2. Explain the difference between a list and a set in Python with examples.
'''
we can access a list using index and also contain duplicates element and enclosed  by "[]" and seperated by ",".
for add the elements in list we use append(values),extend(set,list,tuple,dict),insert(index,valuse)
l=[12,23,24,24,233,24,1,2,23,3]

print(l)
output- [12,23,24,24,233,24,1,2,23,3]

set has no index so we cant access the set using set and set do not contain duplicates elements because set using the hashing technique (hashing technique means each data has unique address), set enclosed by "{}"and seperated by ","
for add the element we use add(value) update(multipla values)
s={12,23,23,23,34,12,34,12,34,5}

print(s)
output- {34, 12, 5, 23}
'''


# 3. Write a Python program to remove duplicates from a list without changing its order.
'''
l=[12,23,24,24,233,24,1,2,23,3]
d=[]
for i in l:
    if i not in d:
        d.append(i)
    
            
print(d)

'''

# 4. How would you iterate over a list and its indices simultaneously in Python?
'''

l=[12,23,24,24,233,24,1,2,23,3]
for i,value in enumerate(l):
    print(i,value)

'''

# 5. Write a Python program to check if all elements in a list are unique.
'''
l=[12,3,2,1,4,5]
s=set(l)
if len(l)==len(s):
    print("its unique list")
else:
    print("its not unique list")
'''

    


# 6. Explain the purpose of the try, except, and finally blocks in Python exception
# handling.



# 7. Write a Python program to read a text file line by line and print each line.
'''
with open("alpha.txt","r+") as f:
    a=f.readlines()
    for i in a:
        
        print(i)

'''
# 8. How can you handle a FileNotFoundError exception while working with files in Python?
''''
try:
    with open ("abc.txt","r") as file:
        a=file.read()
        print(a)
except FileNotFoundError:
    print("file not exist ")
    
'''
    


# 9. Write a Python program to count the number of occurrences of each word in a text file.

    
        


# 10. Explain the difference between the "r", "w", and "a" file modes in Python.
'''

r mode of file handling is used for read a file (only read)
w mode is used for write content in the file (only write)
a mode is used for append the word in the text .(its not override the existing text)

'''

# 11. Write a Python program to find the intersection of two lists using a loop.
'''
a={1,2,3,5,6,5,6,4}
b={9,8,7,6,5,4,3,2}
c=set()
for i in a:
    if i in b:
        c.add(i)
        
print(c)

'''
# 12. How would you handle a KeyError exception while accessing elements in a dictionary?


'''
a=[('a',10),("b",20),('c',30)]
d=dict(a)
try:
    print(d['z'])
    
except KeyError:
    print("key not exist..")

'''


# 13. Write a Python program to read a CSV file and print its contents.
'''
with open ("titanic.csv",'r') as f:
    a=f.readlines()
    for i in a:
        print(i)
        
'''
"""
import csv as c
with open("titanic.csv","r") as f:
    a=c.reader(f)
    for i in a:
        
        print(a)

    """
# 14. Explain the purpose of the enumerate() function in Python with an example.

"""
This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

eg-  eb[("a",3),(12,4)] in this form

    """
# 15. Write a Python program to handle a ValueError exception raised during type
# conversion.

'''
try:
    a=int(input("Enter the number:-"))
    print(a)
    
except ValueError:
    print("plz Enter the values ")

'''
# 16. How can you check if a given element exists in a set?
'''
a={1,2,3,5,6,5,6,4}
b=int(input("Enter the number"))
if b in a:
    print("yes exist")
else:
    print("not exist")
'''

# 17. Write a Python program to find the common elements between two lists using a loop.
'''
a=[12,34,1,23,4,5,6,7]
b=[32,45,6,78,2,34]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)
'''
# 18. Explain the concept of a generator in Python and provide an example.

'''
generator is a special type of function which return iterator using yeild keyword
 
def alpha(n):
    
    yield 1
    yield 2
    
    
print(next(alpha(5)))
print(next(alpha(4)))

'''


# 19. Write a Python program to handle a TypeError exception gracefully.
'''
try:
    a=int(input("Enter the number:- "))
    b=input("Enter number:- ")
    c= a+b
    print(c)

except TypeError:
    c=a+int(b)
    print("its a type conversion of b:- ",c)

'''
# 20. How would you write a list to a file in Python?




# 21. Write a Python program to find the difference between two sets using a loop.
'''
a={1,2,3,5,}
b={9,8,2,4}
c=set()
for i in a:
    if i not in b:
        c.add(i)
        
print(c)


'''

# 22. Explain the purpose of the break and continue statements in Python loops.

'''
# if we want to exits form a particular condition then we use break 
for i in range(5):
    if i==3:
        break
# if we want to skip the particular position then we use continue 
for j in range(5):
    if i==2 or i==4:
        continue
    
'''


# 23. Write a Python program to handle a ZeroDivisionError exception.
'''

try:
    x=int(input("Enter number:- "))
    y=int(input("Enter the number:-"))
    print(x/y)
except ZeroDivisionError:
    
    y=1
    print(x/y)
'''
    

# 24. How can you check if a given list is empty in Python?
'''
a=[]

if len(a)<=0:
    print("list is empty",a)
else:
    print("not empty")
    
'''
    
    

# 25. Write a Python program to append data to a file.
'''
file=open('data.txt','a')
a=input("Enter new data:- ")
file.write(a)
file.close()

'''
# 26. Explain the purpose of the pass statement in Python with an example.
'''
if we dont want to do any changes in the code then use pass for leave as it as .

'''
# 27. Write a Python program to find the maximum and minimum elements in a list using a
# loop.

'''
n=int(input("Enter the range:-"))
x=[]
try:
    for i in range(n):
        a=int(input(f"Enter the value of list {i} index:- "))
        x.append(a)
except ValueError:
    print("please Enter the Values carefully !!!!")
y=set(x)
x=list(y)

for i in range(len(x)):
    for j in range(len(x)):
        if x[i]<=x[j]:
            x[i],x[j]=x[j],x[i]
            
print(x)
print("minimim:- ",x[0])
print("maximun:- ",x[-1])
            

'''


# 28. How would you handle an IndexError exception while accessing elements in a list?

# a=[12,23,34,2]
# try:
#     print(a[3])
#     print(a[5]) #out of index
#     print(a[0])
#     print(a[10]) #out of index
# except IndexError:
#     print("given index is valid:- ")
    

# 29. Write a Python program to create a new directory and save a file in it.

# with open("hello.txt","w+") as f:
#     a=int(input("Enter the number"))
#     x=[]
#     for i in range(a):
#         z=input(f"Enter the {i} values:- ")
#         x.append(z)
        
            
#     print(x)

#     dic=dict(x)
#     f.write(str(dic))

    

# 30. Explain the purpose of the with statement in python file handling.

