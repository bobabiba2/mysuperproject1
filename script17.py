class animals:
    def __init__(self,view, name, age, gender, noise):
        self.view = view
        self.name = name
        self.age = age
        self.gender = gender
        self.noise = noise

cloven_hoofed = animals('cow','Vasya', '2 years','female','Mooo')
print(cloven_hoofed.view)
print(cloven_hoofed.name)
print(cloven_hoofed.age)
print(cloven_hoofed.gender)
print(cloven_hoofed.noise)
rodents = animals('mouse','Petya', '1 year', 'male','pi-pi-pi')
print(rodents.view)
print(rodents.name)
print(rodents.age)
print(rodents.gender)
print(rodents.noise)

class mammals(animals):
    def __init__(self, name, age, gender, noise, wool, temperature, country):
        self.name = name
        self.age = age
        self.gender = gender
        self.noise = noise
        self.wool = wool
        self.temperature = temperature
        self.country = country
    def mamm(self):
        print('Hello, I am mammal :)')
deer = mammals('Cooper', '8 years','male','Foo-Foo', 'thick wool', '38 degrees', 'Russia')
deer.mamm()
class Human(mammals):
    def __init__(self, name, age, gender, work, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.work = work
        self.height = height
        self.weight= weight
Anya = Human('Anya', '22 years', 'female', 'Full-stack dev', '176', '76')
print(Anya.name)
print(Anya.age)
print(Anya.gender)
print(Anya.work)
print(Anya.height)
print(Anya.weight)

class cat(mammals):
    def __init__(self, name, age, gender, breed, noise):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.noise = noise
Dorofei = cat('Dorofei', '11 years', 'male', 'scottish fold', 'Meow-meow')
print(Dorofei.name)
print(Dorofei.age)
print(Dorofei.gender)
print(Dorofei.breed)
print(Dorofei.noise)

class dog(mammals):
    def __init__(self,name, age, gender, breed, noise, home):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.noise = noise
        self.home = home
Palkan = dog('Palkan', '15 years', 'male', 'cur','Woof-Woof','street')
print(Palkan.name)
print(Palkan.age)
print(Palkan.gender)
print(Palkan.breed)
print(Palkan.noise)
print(Palkan.home)