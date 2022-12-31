class Hero:
    name = "Alucard"
    hp = 3000
    damege = 200
    defanse = 100

    def __init__ (self, name, hp, damege, defanse):
        self.name = name
        self.hp = hp
        self.damege = damege
        self.defanse = defanse

    def attack(self, target):
        target.hp = target.hp - self.damege
        print("Sisa HP", target.name, "=", target.hp)

    # inisialisasi class hero
    hero1 = Hero("Hayabusa", 2000, 300, 15)
    hero2 = Hero("Atlas", 3000, 50, 300)

    hero1.attack(hero2)
    hero2.attack(hero1)
