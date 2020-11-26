class Course:

  def __init__(self,course_name,instructor_name):
  	self.course_name = course_name
  	self.instructor_name = instructor_name
  	self.lessons = []



  def add_lesson_time(self,weekday,start_time):
  	t1 = (weekday,start_time)

  	self.lessons.append(t1)


  def print_lesson_times(self):
  	for t in self.lessons:
  		print(t)