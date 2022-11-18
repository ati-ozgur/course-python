
# filename which file should be write
# mode, reading (r), writing (w), appending (a)
# functions read all file
# reading line by line
# reading 10 characters

filename = "JacobsUniversity2022-11-18.txt"

with open(filename, "w",encoding="utf-8") as file:
    file.write("hello from Atilla Özgür")

