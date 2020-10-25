#starcraft

class Unit():
    def __init__(self):
        self.__hp = 40
        self.__mp = 0
        self.x = 0
        self.y = 0
        self.attack_level = 0
        self.defence_level = 3

    def move(self,x,y):
        self.x = x
        self.y = y
        print("({},{})".format(self.x,self.y))

    def attack(self, unit):
        pass

    def stop(self):
        pass

    def set_hp(self,hp):
        __hp = hp

    def get_hp(self):
        print("{}".format(self.__hp))
        return self.__hp

class Worker(Unit):
    
    def build(self,building):
        print(f"{building}을 지었습니다.")

class Soldier(Unit):
    def __init__(self):
        self.__hp = 50
        self.__mp = 10
    pass

class Drone(Worker):
    pass

class Prove(Worker):
    pass

class Scv(Worker):
    def fix(self, unit):
        if type(unit) == '__main__.Scv' or type(unit) == '__main__.Marine':
            unit.__hp += 10

class Zealot(Soldier):
    def attack(self, unit):
        unit.__hp = unit.__hp - (10 - unit.defence_level)

class Marine(Soldier):
    def attack(self, unit):
        unit.__hp = unit.__hp - (8 - unit.defence_level)

scv1 = Scv()
scv1.move(100,50)
a = Marine()
a.attack(scv1)
