

def print_line(numbers):
    line = ""
    for i in numbers:
        line = line + str(i) + "\t"
    print(line)



def grade_school_multiplication_table(n=3):
    for i in range(1, n+1):
        numbers = list(range(1*i, (n+1)*i,i))    
        #print(numbers)
        print_line(numbers)

# range(start,end,increment)

str_N = input("please enter a number for grade school multiplication table")
N = int(str_N)
#N = 10
grade_school_multiplication_table(N)
