# ### 생성자 호출 순서###
# class People:
#     def __init__(self):
#         print("People.__init__()")

# class Athlete(People):
#     def __init__(self):
#         print("Athlete.__init__()")
#         super().__init__()

# class BaseballPlayer(Athlete):
#     def __init__(self):
#         print("BaseballPlayer.__init__()")
#         super().__init__()

# if __name__ == "__main__":
#     people = People()
#     print('----------------')

#     athlete = Athlete()
#     print('----------------')

#     baseball_player = BaseballPlayer()

# #######Override######
# class Animal():
#     def sound(self):
#         print("동물소리")

# class Cat(Animal):
#     def sound(self): #Override
#         print("야옹")

#     def roll(self):
#         print("고양이가 데구르르 구른다.")

# class Dog(Animal):
#     def sound(self): #Override
#         print("왈왈")

#     def walk(self):
#         print("강아지가 총총 걷는다.")

# class Pig(Animal):
#     def sound(self): #Override
#         print("꿀꿀")
    
#     def eat(self):
#         print("돼지가 먹이를 먹는다.")

# if __name__ == "__main__":
#     animal = Animal()
#     cat = Cat()
#     dog = Dog()
#     pig = Pig()
#     animal.sound()
#     cat.sound()
#     cat.roll()
#     dog.sound()
#     dog.walk()
#     pig.sound()
#     pig.eat()

# animals = [cat,dog,pig]
# for obj in animals:
#     obj.sound()
#     if (isinstance(obj,Dog)):
#         obj.walk()

# 다중상속
class Bus():
    def __init__(self):
        print("BUS()")

class Moter():
    def __init__(self):
        print("MOTER()")

class Battery():
    def __init__(self):
        print("BATTERY()")

class ElectronicBus(Bus,Moter,Battery):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    eb = ElectronicBus()