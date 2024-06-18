#ques 1
'''
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
sum=n1+n2
print("sum of",n1,"&",n2,"=",sum)
'''

#ques 2
'''
n=int(input("enter your number:"))
if n%2==0:
    print(n,"is even.")
else:
    print(n,"is odd.")
'''

#ques 3
'''
n=int(input("enter your number:"))
factorial=1
if n==0:
    print("factorial of 0 is = 1")
else:
    for i in range(1,n+1,1):
        factorial*=i
    print("factorial of",n,"is =",factorial)
'''

#ques 4
'''
name=input("enter your name:")
print("Hello",name,"!\nWelcome to Python Programming!")
'''

#ques 7
'''
string=input("enter string:")
print("length of entered string =",len(string))
'''

#ques 8
'''
str1=input("enter first string:")
str2=input("enter second string:")
concatstr=str1+str2
print("concatenated string:",concatstr)
'''

#ques 9
'''
string=input("enter string:")
substr=input("enter substring:")
if substr in string:
    print("substring is present.")
else:
    print("substring is not present.")
'''

#ques 10
'''
string=input("enter your string:")
upperstr=string.upper()
print("string in uppercase:",upperstr)
'''

#ques 12
'''
n=input("enter number:")
l=len(n)
sum=0
for i in range(0,l,1):
    sum+=int(n[i])
print("sum of digits of",n,"is:",sum)
'''

#ques 13
'''
year=int(input("enter birth year:"))
count=0
for i in range(year,2024,1):
    count+=1
print("your age:",count)
'''

#ques 17
'''
string=input("enter string:")
title=string.title()
print("string as title:",title)
'''

#ques 18
'''
string1=input("enter first string:")
string2=input("enter second string:")
list1=[]
list2=[]
for i in range(0,len(string1),1):
    list1.append(string1[i])

for j in range(0,len(string2),1):
    list2.append(string2[j])
list1.sort()
list2.sort()
if list1==list2:
    print("yes strings are anagrams.")
else:
    print("no strings are not anagrams.")
'''

#ques 20
'''
n=int(input("enter no of elements:"))
list1=[]
sum=0
for i in range(1,n+1,1):
    num=int(input("enter number:"))
    sum+=num
    list1.append(num)
print("your list:",list1)
print("sum of elements of list:",sum)
'''

#ques 21
'''
n=int(input("enter no of elements:"))
list1=[]
count=0
for i in range(1,n+1,1):
    element=input("enter element:")
    list1.append(element)
string=input("enter element you want to count:")
for i in range(0,len(list1),1):
    if list1[i]==string:
        count+=1
print("your list:",list1)
print(string,"occured",count,"times.")
'''
#ques 22
'''
n=int(input("enter no of elements:"))
list1=[]
for i in range(1,n+1,1):
    num=int(input("enter number:"))
    list1.append(num)
print("your list:",list1)
list1.sort()
print("max number:",list1[-1])
print("min number:",list1[0])
'''

#ques 23
'''
x=input("enter f for fahrenheit & c for celsius:")
if x=="f":
    temp1=int(input("enter temprature (in fahrenheit):"))
    celsius=((temp1-32)*5)/9
    print("temprature in degree celsius:",celsius)
elif x=="c":
    temp2=int(input("enter temprature (in celsius):"))
    fah=((temp2*9)/5)+32
    print("temprature in degree celsius:",fah)
'''

#ques 24

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
op=input("enter (+,-,*,/):")
if op=="+":
    print("sum:",num1+num2)
elif op=="-":
    print("difference:",num1-num2)
elif op=="*":
    print("product:",num1*num2)
elif op=="/":
    print("division:",num1/num2)
else:
    print("invalid input")

#ques 27
'''
string=input("enter your string:")
list1=[]
for i in range(0,len(string),1):
    list1.append(string[i])
print("list of characters:",list1)
'''



