class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf o'quvchisi.")

student1 = Student("Ali", 15, 9)
student1.info()
