
students = """Name,country
Atilla,Turkey
Daniel,Germany
Ram,India
Veronica,Poland
Ram,India
Daniel,Germany
Daniel,Germany
Daniel,Germany
Ram,India
Veronica,Poland
Ram,India
Veronica,Poland
Veronica,Poland
Veronica,Poland
Ram,India
Bob,USA
"""


d = {}
for student in students.split():
    l = student.split(",")
    name = l[0]
    country = l[1]
    #print(f"name:{name}, country:{country}")
    if country in d:
        d[country] = d[country] + 1
    else:
        d[country] = 1


print(d)