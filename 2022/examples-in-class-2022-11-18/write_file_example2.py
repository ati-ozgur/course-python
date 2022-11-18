
# filename which file should be write
# mode, reading (r), writing (w), appending (a)

filename = "JacobsUniversity2022-11-18.txt"

with open(filename, "a",encoding="utf-8") as file:
    file.writelines("hello ")

