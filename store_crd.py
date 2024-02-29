# with open("data.txt","+a") as f:
#     a=input("Enter your first name:- ")
#     b=int(input("Enter your age:- "))
#     c=input("Enter your email:- ")
#     d=input("Enter your credentials:- ")
#     do=f"name,{a},age,{b},email ,{c},crd ,{d}"
#     dic=f",{ {do} }"
#     f.write(dic)
#     f.close()
    
    
with open("data.txt","r+") as file:
    f=file.readline().split(",")
    
    print(f)
    
    
    