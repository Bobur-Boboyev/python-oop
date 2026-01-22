class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student01 = Student('Bobur', 17, 5)
student02 = Student("Ozod", 16, 5)

print(student01.name)
print(student02.name)