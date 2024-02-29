

# Data types 

# 1. integer -> whole numbers 12,3,4,23,4,45 
# 2.float -> 23.4
# 3.complex  -> 123j
# 4.bool -> true  or false
# 5. collections data types  list [],tuple (),set{},dist{}

# identifiers :

#     should be alphabetic and alphanumeric .
#     spe. symbols not allowed except (_).
#     should not start with numbers .
#     white spaces are not allowed
#     reserve keywords are not allowed


# operators:-

# 1. arithmetic operators  +,-,*,/(float),//(int),%(remainder)
# 2. assignment operators  +=,-=,*=,**=,/=,//=,%=,=
# 3. logical operators     and ,or ,not
# 4. comparision operators <=,>=,<<=,>>=,==
# 5. membership operators in,not in
# 6. bitwise operators and (&),or(|),not(~),xor()
# 7. identity operators  is ,not is

# and ,or
aman="alpha"
passwrd="alpha01"
capture=1122
petname="kuta"
num="998877"
print(capture)
a=input("enter the name and mobile no:- ")
b=input("Enter the password and petname :-\n")
c=int(input("Enter the capture code"))

if a==aman and b== passwrd and c==capture :
    print("permission access")
elif (a==aman or a==num) and (b==passwrd or b==petname) and c==capture:
    print("login accepted....")
else:
    print("login failed... try again..")

