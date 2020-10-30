# # #상속 - 이미 정의된 클래스를 상속받아서 사용하는 방법

# class Parent:
#     def __init__(self):
#         self.a = 10

#     def run(self):
#         print("I am running")

# class Child(Parent):
#     def __init__(self):
#         self.b = 20

# parent = Parent()
# parent.run()

# child = Child()
# child.run()

# class Car:
#     #class variable
#     max_speed = 300
#     max_people = 5

#     def __init__(self):
#         print("Car() 생성자 호출")

#     def __str__(self):
#         print("나는 자동차 입니다.")
    
#     def run(self):
#         print("자동차가 달립니다.")

#     def stop(self):
#         print("자동차가 멈춥니다.")
#         self.stoplight()

#     def stoplight(self):
#         print("브레이크등이 켜졌습니다.")

# class Hybrid(Car):
#     battery_capa = 1000
#     battery_km = 300

# if __name__ == "__main__":
#     niro = Hybrid()
#     print(niro.max_people)
#     niro.stop()

class Car:

    def __init__(self):
        self.gas = 40
        self.speed = 0
        self.max_speed = 300

    def run(self):
        if self.gas>=2:
            self.gas = self.gas - 2
        else:
            print("Gas가 부족합니다.")

        if self.speed<=270:
            self.speed = self.speed + 30
        elif 270<self.speed<self.max_speed:
            self.speed = self.max_speed
        else:
            print("최고속도입니다.")

        print("{}km 속도, {}L 남았습니다.".format(self.speed,self.gas))

    def stop(self):
        if self.speed > 50:
            self.speed = self.speed - 50
        else:
            self.speed = 0
            print("자동차가 멈췄습니다.")

        print(f"{self.speed}km입니다.")

class Hybrid(Car):
    pass

a=Hybrid()
for i in range(11):
    a.run()
for j in range(7):
    a.stop()