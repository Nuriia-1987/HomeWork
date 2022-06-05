# Создать классы машин допустим (Bmw, Mercedes)
# определить такие атрибуты как (title, model, weight, hp, nm, max_speed, color)
# создать метод start_engine() -> output title + model engine started!
# создать метод stop_engine() -> output title + model engine stopped!
# создать метод info() -> All Info

class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"""
Output:{self.title} {self.model} engine started!
                """)

    def stop_engine(self):
        print(f"""
Output: {self.title} {self.model} engine stopped!
                """)

    def all_info(self):
        print(f"""
Title: {self.title} {self.model}
Weihht: {self.weight} 
Hp / Nm: {self.hp} / {self.nm}
Speed: {self.max_speed}
Color: {self.color}
                """)

bmv = Car("BMW", "M5", "2750 кг", 560, 5750, 250, "blue")
bmv.start_engine()
bmv.stop_engine()
bmv.all_info()

merc = Car("Mercedes", "X350", "3250 кг", 258, 3400, 205, "Grey")
merc.start_engine()
merc.stop_engine()
merc.all_info()



