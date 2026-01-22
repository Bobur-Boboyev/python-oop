class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name} — {self.age} yosh")

s1 = Student("Ali", 15)
s2 = Student("Vali", 17)
s3 = Student("Sara", 16)
s4 = Student("Olim", 18)
s5 = Student("Nodira", 14)

students = [s1, s2, s3, s4, s5]

oldest_student = max(students, key=lambda s: s.age)
oldest_student.show_info()

