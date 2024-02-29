print("lets start ...........")

# average
# a=[12,23,43,12,54,66,34]
# c=0
# for i in a:
#     c+=i
# print(c/len(a))

# 
# print(min(a))
# print(max(a))
# b=a.sort()
# print(sort(a))
# print(sum(a))
# print(a.index)    


# minimum
def min_m(a):
    b=0
    for i in a:
        # print(i)
        if b == 0 or i<b:
            b=i
        

    print(f"minimum values is  {b}")


def max_m(a):
    b=0
    for i in a:
        if b==0 or i>=b:
            b=i

    print(f"maximum values is  {b}")

def avg(a):
    add=0
    
    for i in range(len(a)):
        add+=a[i]
    
    ave=add/len(a)

    print(f"average of the numbers:-  {ave}")

def sot(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>=a[j]:
                a[i],a[j]=a[j],a[i]

    print(f"sorted list is {a}")
         
def adding(a):
    count=0
    for i in a:
        count +=i

    print(count)

def multiply(a):
    mul=1
    for i in range(len(a)):
        mul*=a[i]
    print(mul)

def interchange(a,u1,u2):
    a[u1],a[u2]=a[u2],a[u1]
    print(f"interchange numbers{a}")


def sot(a):
    for row in range(len(a)):
        # print("ith index:- ",row)
        for col in range(row,len(a)):
            # print(f"jth index:- {col}")
            
            if a[row]<=a[col]:
                a[row],a[col]=a[col],a[row]
                
    print(a)
        

    

a=[12,23,43,12,54,66,34]
min_m(a)
max_m(a)
avg(a)
sot(a)
adding(a)
multiply(a)
interchange(a,2,4)
# cout(a)
# arm_str(153)

sot(a)