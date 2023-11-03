def say_hello(first_name,last_name):
    print(f"hello {first_name} {last_name}")

# positional arguments calling
#say_hello("Atilla","Özgür")
print("positional arguments calling")
say_hello("Constructor","university")
say_hello("university","Constructor")

# use keyword argument
print("keyword arguments calling")
say_hello(first_name="Constructor", last_name="university")
say_hello(last_name="university", first_name="Constructor", )
