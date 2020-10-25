class Unit:
    def __init__(self, hp = 40, mp = 0, attack_level = 0 , defence_level = 0):
        self.__hp = hp
        self.__mp = mp
        self.__attack_level = attack_level
        self.__defence_level = defence_level
        self.__x, self.__y = 0, 0 

    def move(self, x, y):
        self.__x, self.__y = x, y

    def stop(self):
        print(f"({self.__x}, {self.__y})에 정지하였습니다.")

    def attack(self, enemy):
        enemy_hp = (enemy.get_hp() - (self.__attack_level - enemy.get_defence_level()))
        enemy.set_hp(enemy_hp)

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_mp(self, mp):
        self.__mp = mp

    def get_mp(self):
        return self.__mp

    def set_attack_level(self, attack_level):
        self.__attack_level = attack_level

    def get_attack_level(self):
        return self.__attack_level

    def get_defence_level(self):
        return self.get_defence_level


class Worker(Unit):    
    def __init__(self):
        super().__init__()

    def mine_mineral(self, x, y):
        print(f"({x}, {y})에서 미네랄을 채굴합니다.")

    def build(self, build_name):
        print(f"{build_name}을 지었습니다.")

    def attack(self, enemy):
        print("공격할 수 없습니다.")

class Drone(Worker):
    pass

class Prove(Worker):
    pass

class SCV(Worker):
    def __init__(self,hp = 40, mp = 0, attack_level = 0 , defence_level = 0) :
        super().__init__()
        print(self.get_hp)
    
    def fix(self, unit):
        if ((unit.__class__.__name__== 'SCV') or (unit.__class__.__name__== 'Marine')):
            unit.set_hp(unit.get_hp() + 5) 

class Soldier(Unit):
    def __init__(self, hp = 40, mp = 0, attack_level = 0 , defence_level = 0):
        super().__init__(hp = 50, mp = 10, attack_level = 0, defence_level = 0)

class Zealot(Soldier):
    def __init__(self):
        super().__init__(50, 0, 10, 2)

class Marine(Soldier):
    def __init__(self):
        super().__init__(50, 10, 8, 2)

    def stim_pack(self):
        self.set_mp(self.get_mp - 10)
        self.set_attack_level(self.get_attack_level() + 2)

if __name__ == "__main__":
    scv1 = SCV()
    scv2 = SCV()
    scv1.fix(scv2)
    print(scv1.get_mp())
    print(scv2.get_hp())