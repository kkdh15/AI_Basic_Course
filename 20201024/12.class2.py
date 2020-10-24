# class Car:
#     def __init__(self, maker, model, year):
#         self.maker = maker
#         self.model = model
#         self.year = year
    
#     def set_maker(self,maker):
#         self.maker = maker
    
#     def get_maker(self):
#         return self.maker

#     def print_info(self):
#         print("{}, {}, {}".format(self.maker, self.model, self.year))


# my_car = Car("Hundai","model",2015)
# my_car.print_info()

# my_car.set_maker("BMW")
# my_car.print_info()

# #문제
# Restraunt
# 생성자 : 식당이름, 식당종류, 식당개업연도
# 식당소개() describe_restraunt()
# 식당메뉴소개() 메소드명 자유:
# 식당열기() 메소드명 자유 : 식당이 열렸습니다.
# 식당닫기() 메소드명 자유 : 식당이 닫혔습니다.

# class Restraunt:
#     def __init__(self,name,f_type,year):
#         self.name = name
#         self.f_type = f_type
#         self.year = year
    
#     def describe_restraunt(self):
#         print("{}, {}집이고 {}년에 개업했습니다.".format(self.name,self.f_type,self.year))
    
#     def open(self):
#         print("식당이 열렸습니다.")
    
#     def close(self):
#         print("식당이 닫혔습니다.")

# rst1 = Restraunt("1번식당","한식",2000)
# rst2 = Restraunt("2번식당","일식",2004)
# rst3 = Restraunt("3번식당","중식",2007)

# rst1.describe_restraunt()
# rst2.describe_restraunt()
# rst3.describe_restraunt()

#Starcraft
# SCV : worker
# hp mp attack() move() fix()

# class SCV:
#     def __init__(self, num):
#         self.__hp = 50 # 외부에서 보이지 않음
#         self.__mp = 0
#         self.scv_num = num
#         self.x = 0
#         self.y = 0

#     #getter
#     def get_mp(self):
#         print("{}".format(self.__mp))
#         return self.__mp

#     #setter
#     def set_mp(self,mp):
#         self.__mp = mp
#         print("{}".format(self.__mp))

#     def attack(self, scv):
#         scv.__hp = scv.__hp - 10

#     def fix(self,scv):
#         scv.__hp = scv.__hp + 10

#     def move(self,x,y):
#         self.x = x
#         self.y = y

#     def check(self):
#         print(f"SCV({self.scv_num}) : ({self.__hp}, {self.__mp})")

# scv1 = SCV(1)
# scv2 = SCV(2)
# scv3 = SCV(3)

# scv1.check()
# scv2.check()

# scv1.attack(scv2)

# scv1.check()
# scv2.check()

# scv1.fix(scv2)
# scv1.__hp = 100 # 바뀌지않음

# scv1.check()
# scv2.check()

# scv1.set_mp(10)

# scv1.check()
# scv2.check()

# #문제
# User 클래스
# 캡슐화
# first_name
# last_name
# age
# height
# weight

# set_user(first_name,last_name)
# set_private(age,height,weight)
# describe(user) 
# greet_user() -> 안녕하세요. {이름} 입니다.

class User:
    def __init__(self):
        pass

    def set_user(self,name1, name2):
        self.__first_name = name1
        self.__last_name = name2
    
    def set_private(self,age,height,weight):
        self.__age = age
        self.__height = height
        self.__weight = weight

    def greet_user(self):
        print("안녕하세요. {} {}입니다".format(self.__first_name,self.__last_name))

    def describe(self):
        print("저는 {}살 {}cm {}kg 입니다".format(self.__age,self.__height,self.__weight))

user1 = User()
user1.set_user("Kim","DoHyun")
user1.set_private(21,179,77)
user1.greet_user()
user1.describe()
