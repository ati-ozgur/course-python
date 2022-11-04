import datetime
now =  datetime.datetime.now()
line = f"{now:%Y-%m-%d %B %H:%M:%S}"

print(line)