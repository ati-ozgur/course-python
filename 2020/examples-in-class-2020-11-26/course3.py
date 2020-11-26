class Student:
  def __init__(self,first_name,last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
      return f"{self.first_name} {self.last_name}"

class Course:

  def __init__(self,course_name,instructor_name):
    self.course_name = course_name
    self.instructor_name = instructor_name
    self.lessons = []
    self.student_list = []


  def add_student(self, student):
    self.student_list.append(student)


  def add_lesson_time(self,weekday,start_time):
    t1 = (weekday,start_time)

    self.lessons.append(t1)


  def print_lesson_times(self):
    for t in self.lessons:
      print(t)


  def print_student_list(self):
    for s1 in self.student_list:
      print(s1)