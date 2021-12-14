class Human:
    def __init__(self,name, age, gender, country, weight, height, work, education):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country
        self.weight = weight
        self.height = height
        self.work = work
        self.education = education
class Student(Human):
    def __init__(self,name, age, gender, country, weight, height, work, education, count_homework):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country
        self.weight = weight
        self.height = height
        self.work = work
        self.education = education
        self.count_homework = count_homework
Anya = Student('Anna', '22','female','Russia','176','76','Full Stack dev', 'University','8')
print(Anya.name)
print(Anya.age)
print(Anya.gender)
print(Anya.country)
print(Anya.weight)
print(Anya.height)
print(Anya.work)
print(Anya.education)
print(Anya.count_homework)
