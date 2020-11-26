from course3 import Course,Student



c1 = Course("Programming in Python","Atilla Özgür")


c1.add_lesson_time("Thursday","11:15")
c1.add_lesson_time("Thursday","12:45")
c1.print_lesson_times()


s1 = Student("Yousuf","Farooq")
c1.add_student(s1)



c1.print_student_list()
