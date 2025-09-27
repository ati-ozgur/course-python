class Person:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


    def greeting(self):
        return f"hello, {self.first_name} {self.last_name}"



class Student(Person):
    pass


class Teacher(Person):
    pass




 t1 = Teacher("Atilla","Ozgur")
 print(t1.greeting())
