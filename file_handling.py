# with open("new.txt","a+") as file:
#     user=input("Enter your name:-  ")
#     file.write(user)
#     file.close() 
    
# with open ("new.txt","r") as f:
#     u=f.readline()
#     print(u)
a=int(input("Enter 1 for deposite:- \n 2 for withdrow:-  "))
if a==1:
    with open("pass.txt",'a+') as file:
        
        user=input("Enter your name:- ")
        apass=input("Enter your account_id:- ")
          
        deposite=int(input("Enter your amount to deposite:- "))
        
        file.write(f",{user},{apass},amount,{deposite}")
        file.close()
    
        
        
if a==2:
    user=input("Enter your name:- ")
    apass=input("Enter your account_id:- ")
    
    with open("pass.txt","r+") as f:
        w=int(input("Enter the amount to withdrow:- "))
        ab=f.readline().split(",")
        print(ab)
        dic={}
        
        
        for i in range(0,len(ab),2):
            dic[ab[i]]=ab[i+1]
            
        
            
        # updateing amount after withdrow
        for i in dic.items():
            if user==dic[0] and apass==dic[1]:
                for i in dic.items():
                     dic["amount"]=int(dic["amount"])-w
                
                     
        f.write(f"After_deposite:- {dic['amount']}")
                
        f.close()
                
        
        # withdrow=int(input("Enter amount to withdrow:- "))
        
        