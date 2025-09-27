class Person:
    occupation = ""

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


    def greeting(self):
        return f"hello, I am a {self.occupation} named {self.first_name} {self.last_name}"



class Student(Person):
    occupation = "Student"


class Teacher(Person):
    occupation = "Teacher"



t1 = Teacher("Atilla","Ozgur")
print(t1.greeting())

