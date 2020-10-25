# IS A (상속), HAS A (합성, 집합) #####
class Battery: #has a -> 전기차
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size
        self.battery_balance = 0

    def get_info_battery(self):
        print(f"배터리 사이즈 : {self.battery_size} kwh")
        print(f"배터리 잔  량 : {self.battery_balance} kwh")

    def charge_battery(self,voltage,current):
        self.battery_balance = (voltage * current) * 0.7 / 1000
class Car: #is a -> 전기차
    def __init__(self,maker,model,year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer = 0

    def get_info(self):
        information = f"{self.maker} | {self.model} | {self.year}"

        return information.title()
    
    #getter
    def read_odometer(self):
        print(f"*** {self.odometer}km 입니다. ***")

    #setter
    def update_odometer(self, km):
        if (km > self.odometer):
            self.odometer = km
        else:
            print("주행거리를 변경할 수 없습니다.")

    def increment_odometer(self, km):
        self.odometer += km

class ElectricCar(Car):
    def __init__(self, maker,model, year):
        super().__init__(maker,model,year) #Car().__init__
        self.battery = Battery() #has a 관계 <= 생성자 호출(인스턴스)
    
    #method 추가
    def get_info_battery(self):
        self.battery.get_info_battery()

    def charge_battery(self):
        self.battery.charge_battery(220,5)

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla','model 3',2020)
    print(my_tesla.get_info())
    my_tesla.get_info_battery()
    my_tesla.charge_battery()
    my_tesla.get_info_battery()