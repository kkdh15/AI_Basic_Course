# class
# class 대문자
# class instance 구분

class Dog:
    #생성자 (construct)
    def __init__(self,name,age):
        self.name = name #속성(field)
        self.age = age

    def sit(self):
        print(f"{self.name}가 앉다")
    
    def run(self):
        print(f"{self.name}가 달리다")

    def roll(self):
        print(f"{self.name}가 구르다")

#instance
my_dog = Dog("멍멍이",2)
your_dog = Dog("곰돌이",3)

print("내 강아지는 {}이고, {}살입니다.".format(my_dog.name,my_dog.age))
print("너의 강아지는 {}이고, {}살입니다.".format(your_dog.name,your_dog.age))
