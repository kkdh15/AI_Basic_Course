# # 집합 set 1. 겹치치 않고 2. 순서가 없음
# # dic0 = {} #dictionary
# # dic = {"key":"values"}
# # s = set() #set 초기화

# set1 = {100,200,300,'100',300}
# print(type(set1))
# print(set1)
# print(dir(set1))

# set2 = set()
# print(type(set2))

# set3 = {"apple"}
# set3 = set("apple")
# print(set3)
# print(type(set3))

# set4 = set("ant")
# print(set4)

# print(set3 - set4) #차집합
# print(set3 | set4) #합집합
# print(set3 & set4) #교집합

# #추가
# set5 = set()
# set5.add(100)
# set5.add(200)
# set5.add(300)
# print(set5)
# set5.add(200)
# print(set5)

# set5.update([400,500,100])
# print(set5)

# #삭제 discard remove 
# set5.remove(100)
# print(set5)

# set5.discard(100)
# print(set5)

# #집합 연산자 difference intersection union
# set6 = {'a','b','c','d','e'}
# set7 = {'a','b','c','f','g'}

# set8 = set6.difference(set7) #de 차집합
# print(set8)
# set8 = set6.intersection(set7) #abc 교집합
# print(set8)
# set8 = set6.union(set7) #abcdefg 합집합
# print(set8)

#문제 #음식 궁합 체크 프로그램 ####
#input: 음식 이름을 입력하시오: 
#output: 입력한 음식 떡볶이는 어묵과 궁합이 좋습니다.
#       단, 자료구조에 없으면 다시 질문 받습니다.
foods = {'떡볶이':'어묵',
         '피자':'파스타',
         '라면':'김치',
         '치킨':'맥주',
         '삼겹살':'소주',
         '파전':'막걸리'}

while True:
    a=input("음식 이름을 입력하시오: (" + str(list(foods.keys())) + ") : ")
    if a in foods:
        print("입력한 음식 {0}는 {1}와(과) 궁합이 좋습니다.".format(a,foods.get(a)))
        #print("입력한 음식 "+a+"는 "+foods[a]+"와(과) 궁합이 좋습니다.")
        break
    else:
        print("다시 질문 받겠습니다.")
    
        
        
