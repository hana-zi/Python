class Human:
    def _init_(self,name,birth):
        self.name=name
        self.year=year
    def introduce(self):
        return f'私の名前は{self.name}。今年で{self.year}'

human1=Human('Kawada',26,'19931913')
print(human1.name)
print(human1.introduce())
human2=Human('Yamada',30,'19890703')
print(human2.name)
print(human2.introduce())
human2.grow_old(2)
print(human2.introduce())

class HumanHealth(Human):
    def _init_(self,name,year,birth,height,weight):
        super().__init__(name,year,birth)
        self.height=height
        self.weight=weight


        def get_bmi(self):
            return round(self.weight/(self.height**2).2)

human3=HumanHealth('souma',26,'19931239',1.75,68)
print(human3.get_bmi())
print(human3.introduce())

