print('Hello world!')
#lesson2
class Student:
    amound = 0
    print("Є. Я тут")
    def __init__(self, name = None):
        self.name = name
        Student.amound += 1
    def __str__(self):
        return f'мій логін {self.name}'

class Teacher(Student):
    print('А ну роби домашку!')

dima = Student()
andry = Student()
albina = Teacher()
dima = Student(name = 'DIMAGLOBUS')
print(dima)