# phone numbers for countries

country_information = {}
country_information["DE"] = [49, "Germany", "Federal Republic of Germany"]
country_information["TR"] = [90, "Turkey", "Republic of Turkey"]
country_information["PK"] = [92, "Pakistan", "Islamic Republic of Pakistan"]
country_information["IN"] = [91, "India", "Republic of India"]


info = country_information["IN"]
print(info)

# value !-> key
# from value we can not reach key most of the time

for val in country_information.values():
    print(val)
