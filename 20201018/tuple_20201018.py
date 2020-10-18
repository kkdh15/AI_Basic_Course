# list = []
# tuple = ()
# 읽기전용 -> 수정 삭제 X

t1 = (10,20,30)
print(type(t1))
print(t1)
print(dir(t1))

print(t1.count(10)) # 10과 동일한 항목 갯수 확인
print(t1.index(10)) # 10을 찾아 index 반환

#상수 용도
t2 = 1,2,3
print(type(t2))
print(t2)

t3 = 4 # tuple or value? -> value
t5 = (5) # tuple or value? -> value
print(type(t3))
print(type(t5))

t4 = 5, # ,으로 tuple 
print(type(t4))
t6 =(6,) # tuple
print(type(t6))

# t6.append(7) 추가 안됨
# t1[2] = 40 수정 안됨
# del t1[2] 삭제 안됨

print(t4+t2) #사용법은 동일
print(t2 * 3) #사용법은 동일
print(t2[0] + t2[1])

listA = [1,2,3,4,5]
tupleA = tuple(listA)
print(type(tupleA))

for i in tupleA:
    print(i)

listB = list(tupleA)
print(type(listB))
print(listB)