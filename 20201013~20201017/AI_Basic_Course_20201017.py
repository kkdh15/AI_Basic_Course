# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,6,1):
#         if(i>j):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,6,1):
#         if(i>j):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# a=int(input("First number: "))
# b=int(input("Second number: "))

# max = a if(a>b) else b
# min = a if(a<b) else b

# #최소공배수
# for i in range(max,(a*b)+1,1):
#     if(i%a==0)&(i%b==0):
#         l=i
#         break
# print(l)

# #최대공약수
# for j in range(1,min+1,1):
#     if(a%j==0)&(b%j==0):
#         g=j
#         break
# print(g)

# #각 자리 수 합
# num = int(input("값 입력 : "))
# sum = 0
# while num >= 10:
# 	sum += (num %10)
# 	num = num //10
# sum += num
# print("각  자리의 합 :", sum)

# a=[10,20,30]
# print(type(a))

# for i in a:
#     print(i, end=" ")

# sum=0
# a=list()
# for i in range(0,4,1):
#     b=int(input("임의값 입력: "))
#     a.append(b)
#     sum=sum+a[i]
# print("전체 합: %d" %sum)

#리스트 초기화
# a= [] #list 명은 정했지만 저장 갯수 x
# a= [0,0,0] #list명은 정하고 저장 갯수 3
# a= [0,"kim",True]

# #리스트 병합
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c,len(c))
# d=a
# d.append(b)
# print(d,len(d))

# d.extend(b)
# print(d,len(d))

# #리스트 검색
# string = "my name is kim do hyun"
# index = string.index("kim") #11
# count = string.count("m") #3
# print(index)
# print(count)

# #피보나치 수열
# list=[]
# list.append(1)
# list.append(2)
# sum=3
# for i in range (2,100,1):
#     c=list[i-2]+list[i-1]
#     list.append(c)
#     sum=sum+list[i]
# print(sum)

#lotto 문제 6자리가 안 겹치도록 만드시오.
from random import *
lotto = [0,0,0,0,0,0]
for i in range(0,6,1):
    lotto[i] = randint(1,45)
    for j in range(1,46,1):
        count = lotto.count(j)
        if count >1:
            del lotto[i] #del 하면 범위 줄어짐
            lotto[i]=randint(1,45)
print(lotto)